from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class UserMeasurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey("user.id"))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now())
    chest = db.Column(db.Numeric)
    upper_chest = db.Column(db.Numeric)
    waist = db.Column(db.Numeric)
    hips = db.Column(db.Numeric)
    right_thigh = db.Column(db.Numeric)
    left_thigh = db.Column(db.Numeric)
    right_arm = db.Column(db.Numeric)
    left_arm = db.Column(db.Numeric)
    belly_button = db.Column(db.Numeric)
    stomach = db.Column(db.Numeric)
    weight = db.Column(db.Numeric)

    def __repr__(self):
        return '<Measurement {}-{}>'.format(self.user, self.timestamp)
