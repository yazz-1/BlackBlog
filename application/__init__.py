from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = <secret-key>		# CHANGE THIS
app.config['MONGO_URI'] = <mongoDB-URI>	    # CHANGE THIS


#setup database
client = MongoClient(app.config['MONGO_URI'])
db = client.BlackBlog

from application import routes
