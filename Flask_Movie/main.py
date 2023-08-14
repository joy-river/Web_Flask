from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


header = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZWUzOTk4YWIwOGFhMjM3OTQyMDNkOTA1ZGZlYzczZiIsInN1YiI6IjY0ZDliMmVmMzcxMDk3MDExYzUwOThhZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.4G4eitnkQ4Lv0Z6F9hx7l0Bz1HSasPGJJpWJzXtyP98"
}
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{app.root_path}/Movie.db'
Bootstrap(app)

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class Editform(FlaskForm):
    rating = StringField('Your rating out of 10', validators=[
        DataRequired()])
    review = StringField('Your review',
                         validators=[DataRequired()])
    submit = SubmitField('Submit')


class Addform(FlaskForm):
    movie_name = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    db.create_all()
    return render_template("index.html", movies=db.session.query(Movie).all())


@app.route("/add", methods=["GET", "POST"])
def add():
    form = Addform()
    if form.validate_on_submit():
        movie_title = form.movie_name.data
        response = requests.get(
            url="https://api.themoviedb.org/3/search/movie", headers=header, params={
                "query": movie_title
            })
        return render_template("select.html", data=response.json())
    else:
        return render_template("add.html", form=form)


@app.route('/detail/<int:id>', methods=["GET", "POST"])
def movie_detail(id):
    response = requests.get(
        url=f"https://api.themoviedb.org/3/movie/{id}", headers=header)
    new_movie = Movie(response.text())
    db.session.query(Movie).add(new_movie)
    db.session.commit()
    return app.redirect('/')


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = Editform()
    if form.validate_on_submit():
        db.session.query(Movie).filter_by(id=id).update({
            "rating": form.rating.data,
            "review": form.review.data
        }
        )
        db.session.commit()
        return app.redirect('/')
    else:
        return render_template("edit.html", form=form, movie=Movie.query.get(id))


@app.route("/delete/<int:id>")
def delete(id):
    db.session.query(Movie).filter_by(id=id).delete()
    db.session.commit()
    return app.redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
