from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email
from werkzeug.utils import secure_filename

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "some secret string"


@app.route("/")
def home():
    return render_template('index.html')


class MyForm(FlaskForm):
    Email = StringField(
        label='Email', validators=[Email(), Length(max=30)])
    Password = PasswordField(label='Password', validators=[
        DataRequired(), Length(min=8)])
    Submit = SubmitField('Login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()

    if form.validate_on_submit():
        if form.Email.data == "admin@gmail.com" and form.Password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
