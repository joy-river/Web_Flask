from flask import Flask, render_template
from random import randint
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    ran_num = randint(1, 100)
    return render_template("index.html", random_number=ran_num, time_now=datetime.datetime.now().year,
                           my_name="Joyriver")


@app.route("/guess/<path:username>")
def guess(username):
    agify = requests.get(url=f"https://api.agify.io?name={username}").json()
    genderize = requests.get(url=f"https://api.genderize.io/?name={username}").json()
    return render_template("guess.html", username=username, user_gender=genderize["gender"], user_age=agify["age"])

@app.route("/blog")
def get_blog():
    blog_data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", blog_data=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
