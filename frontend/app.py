from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS if needed


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/list")
def list():
    return render_template("details.html")


if __name__ == "__main__":
    app.run(port=8000)  # Change the port if needed
