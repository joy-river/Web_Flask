from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    return f"<h1>Username: {request.form['username']} Password:{request.form['password']}</h1>"


app.run(debug=True)
