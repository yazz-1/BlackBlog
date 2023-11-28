from application import app, db
from flask import request
import json


@app.route("/")
def index():
	return "He110 w0rld"

@app.route("/post", methods=['POST', 'GET'])
def posts():
	if request.method == 'POST':
		x = {'id': 1,'text': request.form['text']}
		db.tests.insert_one(x)
		return "Done"
	if request.method == 'GET':
		db.tests.find_one({'id': 1})
		return "No problem"
