from flask_wtf import FlaskForm
from wtforms import DecimalField, SubmitField, SelectField
from wtforms.validators import DataRequired
from app.models import User


class EntryForm(FlaskForm):
    users = User.query.all()

    user = SelectField(
        "Person",
        choices=[(u.id, u.name) for u in users],
        validators=[DataRequired()],
        coerce=int
    )
    chest = DecimalField("Chest")
    upper_chest = DecimalField("Upper Chest")
    waist = DecimalField("Waist")
    hips = DecimalField("Hips")
    right_thigh = DecimalField("Right Thigh")
    left_thigh = DecimalField("Left Thigh")
    right_arm = DecimalField("Right Arm")
    left_arm = DecimalField("Left Arm")
    belly_button = DecimalField("Belly Button")
    stomach = DecimalField("Stomach")
    weight = DecimalField("Weight")
    submit = SubmitField("Submit")
