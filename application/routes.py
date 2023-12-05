from application import app, db
from flask import redirect, render_template, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from forms import *
import datetime


@app.route('/')
def index():
	articles = db.articles.find().sort({'_id':-1}).limit(5)
	return render_template('index.html', articles=articles)

@app.route('/<user>/<article_id>')
def get_article_by_ID(user, article_id):
	article = db.articles.find_one({'user': user, 'id': int(article_id)})
	return render_template('article.html', article=article)

@app.route('/<user>')
def get_articles_by_USER(user):
	articles = db.articles.find({'user': user})
	return render_template('user.html', user=user, articles=articles)

@app.route('/post', methods=['GET', 'POST'])
def create_article():

	if 'user' in session:
		form = ArticleForm()
		if form.validate_on_submit():
			try:
				last_id = db.articles.find({'user': form.user.data}).sort({'_id':-1}).limit(1)[0]['id']
			except:
				last_id = 0
			x = {'user': session['user'],
					'id': int(last_id) + 1,
					'title': form.title.data,
					'article': form.article.data,
					'date': datetime.datetime.now(tz=datetime.timezone.utc)
				}
			db.articles.insert_one(x)
			return redirect(url_for('index'))
		else:
			return render_template('post.html', form=form)
	else:
		return "<p>You must be logged in to create an article. You can <a href=" + url_for('login')+ ">Login</a> or <a href=" + url_for('register')+ ">Register</a>.</p>"

@app.route('/edit/<user>/<article_id>', methods=['GET', 'POST'])
def edit_article(user, article_id):
	if 'user' in session:
		if user == session['user']:
			form = EditArticleForm()
			query = {'user': user, 'id': int(article_id)}
			if form.validate_on_submit():
				modified = {'$set': {'title':form.title.data, 'article': form.article.data}}
				db.articles.update_one(query, modified)
				return redirect(url_for('get_article_by_ID', user=user, article_id=article_id))
			else:
				article = db.articles.find_one({'user': user, 'id': int(article_id)})
				return render_template('edit.html', form=form, article=article)
		else:
			return "<h1>Forbidden</h1>", 403
	else:
		return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		x = {'user': form.user.data,
				'password': generate_password_hash(form.password.data),
				'email': form.email.data
			}
		if db.users.find_one({'user':x['user'], 'email':x['email']}) != None:
			print(db.users.find_one({'user':x['user'], 'email':x['email']}))
			return "<p>You already have an account! Log in <a href=" + url_for('login')+ ">here</a></p>"
		elif db.users.find_one({'user':x['user']}) != None:
			return "<p>Username already exists! Please try a new one.<a href=" + url_for('register')+ ">Back</a></p>"
		elif db.users.find_one({'email':x['email']}) != None:
			return "<p>Email already registered! <a href=" + url_for('register')+ ">Back</a></p>"
		else:
			db.users.insert_one(x)
			return "<p>Now you can <a href=" + url_for('login')+ ">Log In</a></p>"
	else:
		return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():

	if 'user' in session:
		return "<p>You are already logged in! Go to <a href=" + url_for('index')+ ">BlackBlog's Home</a></p>"
	else:
		form = LoginForm()
		if form.validate_on_submit():
			x = {'user': form.user.data,
					'password': form.password.data,
				}
			stored = db.users.find_one({'user': x['user']})
			print(check_password_hash(stored['password'], x['password']))
			if not stored or not check_password_hash(stored['password'], x['password']):
				print("Incorrect User or Password")
				return redirect(url_for('login', form=form))
			else:
				session['user_id'] = str(stored['_id'])
				session['user'] = x['user']
				return redirect(url_for('get_articles_by_USER', user=session['user']))
		else:
			return render_template('login.html', form=form)

@app.route('/logout')
def logout():
	session.clear()
	print("Logged Out")
	return redirect(url_for('login'))

@app.route('/about')
def about():
	return render_template('about.html')