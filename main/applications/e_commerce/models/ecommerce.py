from datetime import datetime
from main import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    phone = db.Column(db.String(30))
    password = db.Column(db.String(100), nullable=False)
    date_joined = db.Column(db.Datetime, nullable=False,
                            default=datetime.utcnow)
    modified = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)
    type = db.Column(db.Integer, nullable=False)
    deleted = db.Column(db.Boolean, nullable=False, default=False)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column()
    address1 = db.Column(db.String(100))
    address2 = db.Column(db.String(100))


class PostalCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(255), nullable=False)


class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    product_details_id = db.Column(db.Integer, nullable=False)
    saved_for_later = db.Column(db.Boolean, nullable=False, default=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    time_added = db.Column(db.Integer, default=datetime.utcnow)


class ProductDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(100), nullable=False)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(Db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullabe=False)
    price = db.Column(db.Integer, nullable=False)


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    tag = db.Column(db.String(255), nullable=False)


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    address_id = db.Column(db.Integer, nullable=False)
    discount_id = db.Column(db.Integer, nullable=False)
    created = db.Column(db.Datetime, default=datetime.utcnow)
    modified = db.Column(db.Datetime, default=datetime.utcnow)
    status = db.Column(db.Enum("Status1", "Status2", name="status_category"))
    amount = db.Column(db.Integer, nullable=False)


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    product_details_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


class Discount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    discount = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer)
    created = db.Column(db.Datetime, default=datetime.utcnow)
    valid = db.Column(db.Datetime, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.String(db.String(255), nullable=False)
