from flask import render_template
from . import create_app

app = create_app()


@app.route("/")
def home():
    print("Hello")
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/upload")
def upload():
    return render_template("upload.html")
