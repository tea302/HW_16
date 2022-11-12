import json

from flask import request
from flask_sqlalchemy import SQLAlchemy
from app import app
from new.database_init import init_database
from new.models import User, Order, Offer

db = SQLAlchemy(app)


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        result = []
        for u in User.query.all():
            result.append(u.to_dict())

        return json.dumps(result), 200, {'Content-Type': 'application/json; charset=utf-8'}

    if request.method == "POST":
        user_data = json.loads(request.data)

        db.session.add(
            User(
                id=user_data.get("id"),
                first_name=user_data.get("first_name"),
                last_name=user_data.get("last_name"),
                age=user_data.get("age"),
                email=user_data.get("email"),
                role=user_data.get("role"),
                phone=user_data.get("phone"),
            )
        )
        db.session.commit()

        return "", 201


@app.route("/users/<int:uid>", methods=["GET", "PUT", "DELETE"])
def user(uid: int):
    if request.method == "GET":
        return json.dumps(User.query.get(uid).to_dict()), 200, {'Content-Type': 'application/json; charset=utf-8'}
    if request.method == "PUT":
        user_data = json.loads(request.data)
        u = User.query.get(uid)

        u.first_name = user_data["first_name"]
        u.last_name = user_data["last_name"]
        u.age = user_data["age"]
        u.email = user_data["email"]
        u.role = user_data["role"]
        u.phone = user_data["phone"]

        db.session.add(u)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        u = User.query.get(uid)

        db.session.delete()
        db.session.commit()

        return "", 204


@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        result = []
        for u in Order.query.all():
            result.append(u.to_dict())

        return json.dumps(result), 200, {'Content-Type': 'application/json; charset=utf-8'}
    if request.method == "POST":
        order_data = json.loads(request.data)

        db.session.add(
            Order(
                id=order_data.get("id"),
                name=order_data.get("name"),
                description=order_data.get("description"),
                start_data=order_data.get("start_data"),
                end_data=order_data.get("end_data"),
                address=order_data.get("address"),
                price=order_data.get("price"),
                customer_id=order_data.get("customer_id"),
                executer_id=order_data.get("executer_id"),
            )
        )
        db.session.commit()

        return "", 201


@app.route("/orders/<int:uid>", methods=["GET", "PUT", "DELETE"])
def order(uid: int):
    if request.method == "GET":
        return json.dumps(Order.query.get(uid).to_dict()), 200, {'Content-Type': 'application/json; charset=utf-8'}
    if request.method == "PUT":
        order_data = json.loads(request.data)
        u = Order.query.get(uid)

        u.name = order_data["name"]
        u.description = order_data["description"]
        u.start_data = order_data["start_data"]
        u.end_data = order_data["end_data"]
        u.address = order_data["address"]
        u.price = order_data["price"]
        u.customer_id = order_data["customer_id"]
        u.executer_id = order_data["executer_id"]

        db.session.add(u)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        u = Order.query.get(uid)

        db.session.delete()
        db.session.commit()

        return "", 204


@app.route("/offers", methods=["GET", "POST"])
def offers():
    if request.method == "GET":
        result = []
        for u in Offer.query.all():
            result.append(u.to_dict())

        return json.dumps(result), 200, {'Content-Type': 'application/json; charset=utf-8'}
    if request.method == "POST":
        offer_data = json.loads(request.data)

        db.session.add(
            Offer(
                id=offer_data.get("id"),
                order_id=offer_data.get("order_id"),
                executer_id=offer_data.get("executer_id"),
            )
        )
        db.session.commit()

        return "", 201


@app.route("/offers/<int:uid>", methods=["GET", "PUT", "DELETE"])
def offer(uid: int):
    if request.method == "GET":
        return json.dumps(Offer.query.get(uid).to_dict()), 200, {'Content-Type': 'application/json; charset=utf-8'}
    if request.method == "PUT":
        offer_data = json.loads(request.data)
        u = Offer.query.get(uid)

        u.order_id = offer_data["order_id"]
        u.executer_id = offer_data["executer_id"]

        db.session.add(u)
        db.session.commit()

        return "", 201

    if request.method == "DELETE":
        u = Offer.query.get(uid)

        db.session.delete()
        db.session.commit()

        return "", 204


if __name__ == '__main__':
    init_database()
    app.run(debug=True)
