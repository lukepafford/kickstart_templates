#!/usr/bin/env python
from flask import Flask, render_template, request, abort, make_response
import json, logging, os, sys

app = Flask(__name__)

@app.route('/')
def ks():
	context = dict()
	creds = read_creds()
	context.update(**creds)
	hostname = request.args.get('hostname')

	if not hostname:
		abort(400, '"hostname" must be set in query arguments')
	else:
		context['hostname'] = hostname
		response = make_response(render_template('ks.cfg', **context))
		response.mimetype = 'text/plain'
		return response

def read_creds():
	creds_file = os.path.join(os.getcwd(), 'data.json')
	with open(creds_file) as f:
		creds = json.load(f)
	return creds
