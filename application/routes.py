from application import app, db
from flask import request, render_template
from forms import ArticleForm
import datetime


@app.route("/")
def index():
	posts = db.tests.find()
	return render_template('index.html', posts=posts)

@app.route("/post", methods=['POST', 'GET'])
def post():
	form = ArticleForm()
	if form.validate_on_submit():
		x = {'user': form.user.data,
				'title': form.title.data,
				'text': form.text.data,
				'date': datetime.datetime.now()
			}
		db.tests.insert_one(x)
		return render_template('post.html', form=form)
	else:
		return render_template('post.html', form=form)