from app import app, db
from flask import render_template, flash, redirect
from app.models import User, UserMeasurement
from app.forms import EntryForm
import datetime


@app.route('/', methods=['GET', 'POST'])
def entry():
    form = EntryForm()
    if form.validate_on_submit():
        record = UserMeasurement(
            user=form.user.data,
            timestamp=datetime.datetime.now(),
            chest=form.chest.data,
            upper_chest=form.upper_chest.data,
            waist=form.waist.data,
            hips=form.hips.data,
            right_thigh=form.right_thigh.data,
            left_thigh=form.left_thigh.data,
            right_arm=form.right_arm.data,
            left_arm=form.left_arm.data,
            belly_button=form.belly_button.data,
            stomach=form.stomach.data,
            weight=form.weight.data
        )
        db.session.add(record)
        db.session.commit()
        u = User.query.get(form.user.data)
        flash("Record added for {}".format(u.name))

        return redirect('/')

    users = User.query.all()

    context = {
        'form': form,
        'users': users,
        'route': "entry"
    }

    return render_template("entry.html", context=context)


@app.route('/progress/<user_id>')
def progress(user_id):

    users = User.query.all()
    user = next(u for u in users if u.id == int(user_id))
    labels = [
        'Chest',
        'Upper Chest',
        'Waist',
        'Hips',
        'Right Thigh',
        'Left Thigh',
        'Right Arm',
        'Left Arm', 
        'Belly Button', 
        'Stomach',
        'Weight'
    ]
    fields = ['_'.join(l.lower().split(' ')) for l in labels]

    data = UserMeasurement.query.filter_by(user=int(user_id)).all()
    table_data = data[-3:]
    chart_data = {
        f: [str(d.__getattribute__(f)) for d in data[-10:]] for f in fields
    }
    chart_data['timestamps'] = [d.timestamp for d in data]

    context = {
        'full_data': data,
        'data_len': len(data),
        'table_data': table_data, 
        'chart_data': chart_data,
        'user': user,
        'users': users,
        'labels': labels,
        'fields': fields,
        'route': 'progress' + user.name
    }

    return render_template('progress.html', context=context)
