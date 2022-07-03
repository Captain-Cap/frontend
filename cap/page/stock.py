from collections import namedtuple
from datetime import datetime
from typing import Any

from flask import Blueprint, redirect, render_template, request, url_for

from cap.api import BalloonModel, client
from cap.forms import AddBalloonForm

stock = Blueprint('stock', __name__)


@stock.get('/')
def all_balloons():
    balloons = client.balloons.get_all()
    projects = client.projects.get_all()
    projects_map = {project.uid: project for project in projects}
    card_project = namedtuple('card_project', 'balloon name_project')

    colors = []
    for bal in balloons:
        if bal.color not in colors:
            colors.append(bal.color)

    models = []
    for balloon in balloons:
        if projects_map.get(balloon.project_id):
            models.append(card_project(
                balloon,
                projects_map.get(balloon.project_id).name,
            ))
        else:
            models.append(card_project(
                balloon,
                'No project',
            ))

    return render_template(
        'stock.html',
        title='Balloons',
        colors=colors,
        balloons=models,
        projects=projects,
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
