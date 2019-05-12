from app import app, db
from flask import render_template, flash, redirect
from app.models import User, UserMeasurement
from app.forms import EntryForm

@app.route('/', methods=['GET', 'POST'])
def entry():
    form = EntryForm()
    if form.validate_on_submit():
        record = UserMeasurement(
            user = form.user.data,
            chest = form.chest.data,
            upper_chest = form.upper_chest.data,
            waist = form.waist.data,
            hips = form.hips.data,
            right_thigh = form.right_thigh.data,
            left_thigh = form.left_thigh.data,
            right_arm = form.right_arm.data,
            left_arm = form.left_arm.data,
            belly_button = form.belly_button.data,
            stomach = form.stomach.data,
            weight = form.weight.data
        )
        db.session.add(record)
        db.session.commit()
        u = User.query.get(form.user.data)
        flash("Record added for {}".format(u.name))
        return redirect('/')

    return render_template("entry.html", form=form)