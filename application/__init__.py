from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "5569f02c22d1939f85a1530a1c9d330a80f73b7f"
app.config["MONGO_URI"] = "mongodb+srv://yazz1:sO3Avzbakv80aBAy@cluster0.051rnmh.mongodb.net/?retryWrites=true&w=majority"


#setup database
mongodb_client = PyMongo(app)
db = mongodb_client.db


from application import routes