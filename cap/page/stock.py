from datetime import datetime
from distutils.util import strtobool
from typing import Any

from flask import Blueprint, redirect, render_template, request, url_for

from cap.api import BalloonModel, client
from cap.api.schemas import ProjectsModel
from cap.forms import AddBalloonForm

stock = Blueprint('stock', __name__)


@stock.get('/')
def all_balloons():
    projects = get_projects_map()
    balloons = client.balloons.get_all()

    models = [to_model(balloon, projects) for balloon in balloons]
    colors = {balloon.color for balloon in balloons}

    return render_template(
        'stock.html',
        title='Balloons',
        colors=colors,
        balloons=models,
        projects=projects,
        form=AddBalloonForm(),
    )


def filter_color(balloons, color: str) -> list[BalloonModel]:
    if color == 'No color':
        return balloons

    return [balloon for balloon in balloons if balloon.color == color]


def to_model(
    balloon: BalloonModel,
    projects: dict[int, ProjectsModel],
) -> tuple[BalloonModel, str]:
    project = projects[balloon.project_id] if balloon.project_id else None
    project_name = project.name if project else 'No project'
    return balloon, project_name


def get_projects_map():
    projects = client.projects.get_all()
    return {project.uid: project for project in projects}


@stock.post('/sort')
def sort():
    payload = dict(request.form)
    projects = get_projects_map()

    freeonly = bool(strtobool(payload['flexRadio']))
    if freeonly:
        balloons = client.balloons.get_free()
    else:
        balloons = client.balloons.get_all()

    selected_color = payload['Color']
    filtered_balloons = filter_color(balloons, selected_color)

    models = [to_model(balloon, projects) for balloon in filtered_balloons]
    colors = {balloon.color for balloon in balloons}

    return render_template(
        'stock.html',
        colors=colors,
        balloons=models,
        projects=projects.values(),
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
