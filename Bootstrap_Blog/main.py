from flask import Flask, render_template
import deco

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<filename>")
def redirect(filename):
    return render_template(f"{filename}", filename=filename[0:-5])


if __name__ == "__main__":
    app.run(debug=True)
