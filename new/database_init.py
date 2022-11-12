from flask_sqlalchemy import SQLAlchemy
import raw_data
from app import app
from new.models import User, Order, Offer

db = SQLAlchemy(app)


def init_database():
    app.app_context().push()
    with app.app_context():
        db.drop_all()
        db.create_all()

    for user_data in raw_data.users:
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

    for order_data in raw_data.orders:
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

    for offer_data in raw_data.offers:
        db.session.add(
            Offer(
                id=offer_data.get("id"),
                order_id=offer_data.get("order_id"),
                executer_id=offer_data.get("executer_id"),
            )
        )
        db.session.commit()
