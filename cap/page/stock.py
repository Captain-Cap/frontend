from datetime import datetime
from typing import Any

from flask import Blueprint, redirect, render_template, request, url_for

from cap.api.balloons import BalloonApi
from cap.api.schemas import BalloonModel
from cap.config import config
from cap.forms import AddBalloonForm

balloon_api = BalloonApi(config.url)

stock = Blueprint('stock', __name__)


@stock.get('/')
def all_balloons():
    balloons = balloon_api.get_all()
    return render_template(
        'stock.html',
        title='Balloons',
        balloons=balloons,
        form=AddBalloonForm(),
    )


@stock.post('/add_balloon')
def add_balloon():
    payload: dict[str, Any] = request.form
    payload['uid'] = -1
    payload['acceptance_date'] = datetime.now()

    balloon = BalloonModel(**request.form)
    balloon_api.add(balloon)

    return redirect(url_for('stock.all_balloons'))


@stock.post('/delete')
def delete():
    uid = request.form['uid']
    balloon_api.delete(uid)
    return redirect(url_for('stock.all_balloons'))
