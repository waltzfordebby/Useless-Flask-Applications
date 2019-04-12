from main import db


class Holiday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey(
        'holiday_type.id'), nullable=False)

    def __repr__(self):
        return f"Holiday('{self.date}', '{self.name}')"


class HolidayType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    holidays = db.relationship("Holiday", backref="type", lazy=True)

    def __repr__(self):
        return f"HolidayType('{self.name}')"
