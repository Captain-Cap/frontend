from datetime import datetime
from typing import Any

from flask import Blueprint, redirect, render_template, request, url_for

from cap.api import BalloonModel, client
from cap.forms import AddBalloonForm

stock = Blueprint('stock', __name__)


@stock.get('/')
def all_balloons():
    balloons = client.balloons.get_all()
    return render_template(
        'stock.html',
        title='Balloons',
        balloons=balloons,
        form=AddBalloonForm(),
    )


@stock.post('/add_balloon')
def add_balloon():
    payload: dict[str, Any] = dict(request.form)
    payload['uid'] = -1
    payload['acceptance_date'] = datetime.now()

    balloon = BalloonModel(**payload)
    client.balloons.add(balloon)

    return redirect(url_for('stock.all_balloons'))


@stock.post('/delete')
def delete():
    uid = request.form['uid']
    client.balloons.delete(uid)
    return redirect(url_for('stock.all_balloons'))


@stock.get('/edit/<int:uid>')
def edit_page(uid):
    balloon = client.balloons.get_by_id(uid)
    return render_template('stock_edit.html', balloon=balloon)


@stock.post('/edit/<int:uid>')
def edit(uid):
    payload: dict[str, Any] = dict(request.form)
    payload['uid'] = uid
    payload['acceptance_date'] = -1
    balloon = BalloonModel(**payload)
    client.balloons.update(balloon)
    return redirect(url_for('stock.all_balloons'))
