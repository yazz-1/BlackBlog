from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = <secret-key>		# CHANGE THIS
app.config["MONGO_URI"] = <mongoDB-URI>		# CHANGE THIS


#setup database
mongodb_client = PyMongo(app)
db = mongodb_client.db

if not 'tests' in db.list_collections():
	tests_collection = db['tests']

if not 'articles' in db.list_collections():
	articles_collection = db['articles']


from application import routes
