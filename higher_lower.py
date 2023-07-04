from flask import Flask
import random

app = Flask(__name__)

answer = random.randint(0, 9)


def deco_align(func):
    def wrap_deco(**kwargs):
        text = f'<div style="text-align:center">{func(**kwargs)}</div>'
        return text

    return wrap_deco


@app.route("/")
@deco_align
def Init():
    return "<h1>Choose Your Number! in {0 ~ 9}</h1>" \
           "<img src='https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp'>"


@app.route("/<int:guess>", endpoint='guess')
@deco_align
def redirect(guess):
    if guess > answer:
        return "<h1>Too High. Try Again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif guess < answer:
        return "<h1>Too Low. Try Again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return f"<h1>Correct! The answer is {answer}!</h1>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == '__main__':
    app.run(debug=True)
