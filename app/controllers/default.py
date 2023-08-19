from flask import render_template
from app import app

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/arts")
def arts():
    return render_template("arts.html")

@app.route("/apps")
def apps():
    return render_template("apps.html")

@app.route("/web_sites")
def web_sites():
    return render_template("web-site.html")