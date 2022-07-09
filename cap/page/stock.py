from collections import namedtuple
from datetime import datetime
from typing import Any

from distutils.util import strtobool

from flask import Blueprint, redirect, render_template, request, url_for

from cap.api import BalloonModel, client
from cap.forms import AddBalloonForm
from cap.page.attributes import attributes

stock = Blueprint('stock', __name__)


@stock.get('/')
def all_balloons():
    projects = client.projects.get_all()
    card_project = namedtuple('card_project', 'balloon name_project')

    models = [card_project(*model) for model in attributes.balloon.all(status=True)]
    colors = attributes.balloon.color_from([model.balloon for model in models])

    return render_template(
        'stock.html',
        title='Balloons',
        colors=colors,
        balloons=models,
        projects=projects,
        form=AddBalloonForm(),
    )


@stock.post('/sort')
def sort():
    payload = dict(request.form)
    card_project = namedtuple('card_project', 'balloon name_project')

    models = [
        card_project(*model)
        for model in attributes.balloon.all(status=bool(strtobool(payload['flexRadio'])))
    ]
    colors = attributes.balloon.color_from([model.balloon for model in models])
    entity = attributes.balloon.by_color(models, payload['Color'])

    return render_template(
        'stock.html',
        colors=colors,
        balloons=entity,
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
    projects = client.projects.get_all()
    return render_template('stock_edit.html', balloon=balloon, projects=projects)


@stock.post('/edit/<int:uid>')
def edit(uid):
    payload: dict[str, Any] = dict(request.form)
    payload['uid'] = uid
    payload['acceptance_date'] = -1
    balloon = BalloonModel(**payload)
    client.balloons.update(balloon)
    return redirect(url_for('stock.all_balloons'))
