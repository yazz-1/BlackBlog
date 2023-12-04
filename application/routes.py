from application import app, db
from flask import redirect, render_template, url_for
from forms import ArticleForm, EditArticleForm
import datetime


@app.route("/")
def index():
	articles = db.articles.find().sort({'_id':-1}).limit(5)
	return render_template('index.html', articles=articles)

@app.route("/<user>/<article_id>")
def get_article_by_ID(user, article_id):
	article = db.articles.find_one({'user': user, 'id': int(article_id)})
	return render_template('article.html', article=article)

@app.route("/<user>/")
def get_articles_by_USER(user):
	articles = db.articles.find({'user': user})
	return render_template('user.html', user=user, articles=articles)

@app.route("/post", methods=['POST', 'GET'])
def create_article():
	form = ArticleForm()
	if form.validate_on_submit():
		try:
			last_id = db.articles.find({'user': form.user.data}).sort({'_id':-1}).limit(1)[0]['id']
		except:
			last_id = 0
		x = {'user': form.user.data,
				'id': int(last_id) + 1,
				'title': form.title.data,
				'article': form.article.data,
				'date': datetime.datetime.now(tz=datetime.timezone.utc)
			}
		db.articles.insert_one(x)
		return redirect(url_for('index'))
	else:
		return render_template('post.html', form=form)

@app.route("/edit/<user>/<article_id>", methods=['GET', 'POST'])
def edit(user, article_id):
	form = EditArticleForm()
	query = {'user': user, 'id': int(article_id)}
	if form.validate_on_submit():
		modified = {'$set': {'title':form.title.data, 'article': form.article.data}}
		db.articles.update_one(query, modified)
		return redirect(url_for('get_article_by_ID', user=user, article_id=article_id))
	else:
		article = db.articles.find_one({'user': user, 'id': int(article_id)})
		return render_template('edit.html', form=form, article=article)

@app.route("/about")
def about():
	return render_template('about.html')