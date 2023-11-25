from application import app
from flask import request
import json


@app.route("/")
def index():
	return "He110 w0rld"

@app.route("/login", methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		x = {'method': 'POST'}
		return json.dumps(x)
	if request.method == 'GET':
		x = {'method': 'GET'}
		return json.dumps(x)