from app import app, db
from flask import render_template, redirect, url_for, flash, jsonify, Response
from app.models import Service
import json

@app.route('/', methods = ['GET', 'POST'])
def index():
	return render_template('index.html')


@app.route('/loaddata', methods = ['GET'])
def loaddata():
	data = Service.query.all()
	res = jsonify(json_list=[i.serialize for i in data])
	print(res.get_data())
	return res