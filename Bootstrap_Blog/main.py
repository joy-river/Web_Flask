import pprint
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return app.redirect("/index.html")


@app.route("/<filename>")
def redirect(filename):
    return render_template(f"{filename}", filename=filename[0:-5], posts=posts)


posts = requests.get(url="https://api.npoint.io/fc3f961b4a897e129960").json()


@app.route("/post/<int:post_id>")
def show_a_post(post_id):
    return render_template("post.html", post=posts[post_id - 1])


if __name__ == "__main__":
    app.run(debug=True)
