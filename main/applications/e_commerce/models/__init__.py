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
