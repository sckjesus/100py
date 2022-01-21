import time
import os
import flask
from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix

app = flask.Flask(__name__)

@app.route("/a_new_url")
def new_url():
    return 'This is a new location!'

@app.route("/")
def starting_url():
    print("tfvjghj")
    return flask.redirect("/a_new_url")
app.run()