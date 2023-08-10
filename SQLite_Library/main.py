from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy, session


app = Flask(__name__)

# db = sqlite3.connect("SQLite_Library/books-collection.db")

# cursor = db.cursor()

# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")


# cursor.execute(
#     "INSERT or IGNORE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# db.close()
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{app.root_path}/Library.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

# # CRUD with sqlalchemy
# # Create
# # Read
# # Update
# # Delete
# with app.app_context():
#     #Create db
#     db.create_all()
#     new_book = Book(title="Parry Hotter",
#                     author="J. R. Kowling", rating="9.3")
#     db.session.add(new_book)
#     db.session.commit()

#     # Read all records from db
#     all_books = db.session.query(Book).all()

#     # Search db by argument.
#     book = Book.query.filter_by(title="Parry Hotter").first()

#     # Update record
#     book_to_update = Book.query.filter_by(title="Parry Hotter").first()
#     book_to_update.title = "Parry Hotter and the Shamber of Cecrets"

#     # Update record by id
#     book_id = 1
#     book_to_update = Book.query.get(book_id)
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()

#     # Delete record by id
#     book_id = 1
#     book_to_delete = Book.query.get(book_id)
#     db.session.delete(book_to_delete)


@app.route('/')
def home():
    db.create_all()
    return render_template("index.html", books=db.session.query(Book).all())


@app.route('/<int:id>')
def delete(id):
    db.session.query(Book).filter_by(id=id).delete()
    db.session.commit()
    return app.redirect('/')


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return app.redirect("/")
    else:
        return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        db.session.query(Book).filter_by(
            id=id).update({
                'rating': request.form['rating']}
        )
        db.session.commit()
        return app.redirect('/')
    else:
        return render_template("edit.html", book=Book.query.get(id))


if __name__ == "__main__":
    app.run(debug=True)
