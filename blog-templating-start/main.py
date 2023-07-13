from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
blog_data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
@app.route('/')
def home():
    return render_template("index.html", blog_data=blog_data)

@app.route("/post/<id>")
def get_post(id):
    post = Post(blog_data[int(id) - 1])
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
