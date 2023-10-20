from flask import Flask, json, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{app.root_path}/cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_json(self):
        cafe = self
        return {
            'id': cafe.id,
            'name': cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            'has_wifi': cafe.has_wifi,
            'has_sockets': cafe.has_sockets,
            'can_take_calls': cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
        }


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    cafe = random.choice(db.session.query(Cafe).all())
    return cafe.to_json()


@app.route("/all")
def all_cafe():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_json() for cafe in cafes])


@app.route("/search")
def search_cafe():
    query_loc = request.args.get("loc")
    cafes = db.session.query(Cafe).filter_by(location=query_loc).all()
    if len(cafes) > 0:
        return jsonify(cafes=[cafe.to_json() for cafe in cafes])
    else:
        return {"error": {
                "Not Found": "Sorry, we don't have a cafe at the location."
                }}

# HTTP POST - Create Record


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return {
        "response": {
            "success": "Successfully added the new cafe."
        }
    }
# HTTP PUT/PATCH - Update Record


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    price = request.args.get("price")
    if cafe:
        cafe.coffee_price = price
        db.session.commit()
        return {
            "success": "Successfully updated the price."
        }
    else:
        return {
            "error": f"Sorry, there is no cafe with id={cafe_id}"
        }
# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
