from flask import Flask
from pymongo import MongoClient
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = <secret-key>		# CHANGE THIS
app.config['MONGO_URI'] = <mongoDB-URI>	    	# CHANGE THIS
app.permanent_session_lifetime = timedelta(minutes=30)
app.url_map.strict_slashes = False

#setup database
client = MongoClient(app.config['MONGO_URI'])
db = client.BlackBlog

from application import routes
