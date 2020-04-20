#!/usr/bin/env python
from flask import Flask, render_template, request, abort, make_response
import json, logging, os, sys

app = Flask(__name__)


@app.route("/")
def ks():
    context = dict()
    data = read_data()
    context.update(**data)
    hostname = request.args.get("hostname")

    if not hostname:
        abort(400, '"hostname" must be set in query arguments')
    else:
        context["hostname"] = hostname
        response = make_response(render_template("ks.cfg", **context))
        response.mimetype = "text/plain"
        return response


def read_data():
    data_file = os.path.join(os.getcwd(), "data.json")
    with open(data_file) as f:
        data = json.load(f)
    return data
