from flask import Flask
import random

app = Flask(__name__)

answer = random.randint(0, 9)
@app.route("/")
def Init():
    return "Choose Your Number! in {0 ~ 9}"



if __name__ == '__main__':
    app.run(debug=True)