from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.fields import StringField
from wtforms.validators import Length, DataRequired, Optional
from werkzeug.utils import secure_filename


app = Flask(__name__)

app.secret_key = "some secret string"


@app.route("/")
def home():
    return render_template('index.html')


class UploadForm(FlaskForm):
    upload = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])


class MyForm(FlaskForm):
    name = StringField(
        'Full Name', [DataRequired(), Length(max=10)])
    address = StringField('Mailing Address', [
                          Optional(), Length(max=200)])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()

    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(app.os.path.join(
            app.instance_path, 'photos', filename
        ))
        return app.redirect(app.url_for('index'))

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
