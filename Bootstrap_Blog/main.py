from flask import Flask, render_template, request
import requests
import email_module

app = Flask(__name__)


@app.route("/")
def home():
    return app.redirect("/index")


@app.route("/<filename>")
def redirect(filename):
    if ".html" in filename:
        return app.redirect(f"/{filename[0:-5]}")
    else:
        return render_template(f"{filename}.html", filename=filename, posts=posts)


posts = requests.get(url="https://api.npoint.io/fc3f961b4a897e129960").json()


@app.route("/post/<int:post_id>")
def show_a_post(post_id):
    return render_template("post.html", post=posts[post_id - 1])


@app.route("/contact", methods=["GET", "POST"])
def form_data():
    if request.method == "POST":
        email_module.send_email(request.form)
        return render_template("contact.html", filename="contact", post=True)
    elif request.method == "GET":
        return render_template("contact.html", filename="contact")


if __name__ == "__main__":
    app.run(debug=True)
