from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for

from cap.api.balloons import BalloonApi
from cap.model.forms import AddBalloonForm
from cap.model.schemas import BalloonModel

balloon_api = BalloonApi()

stock = Blueprint('stock', __name__)


@stock.get('/')
def all_balloons():
    context = {
        'title': 'Balloons',
        'list_balloons': balloon_api.get_all(),
        'form': AddBalloonForm(),
    }
    return render_template('stock.html', context=context)


@stock.post('/')
def add_balloon():
    balloon = dict(request.form)
    balloon.pop('csrf_token')
    balloon.pop('submit')
    payload = BalloonModel(
        firm=balloon['firm'],
        paint_code=balloon['paint_code'],
        color=balloon['color'],
        volume=balloon['volume'],
        weight=balloon['weight'],
        acceptance_date=str(datetime.now()),
    )
    balloon_api.add(payload)
    return redirect(url_for('stock.all_balloons'))
