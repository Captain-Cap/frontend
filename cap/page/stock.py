from datetime import datetime
from typing import Any

from flask import Blueprint, redirect, render_template, request, url_for

from cap.api import BalloonModel, client
from cap.api.schemas import ProjectsModel

stock = Blueprint('stock', __name__)


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



@stock.get('/')
def all_balloons():
    projects = get_projects_map()

    free_only = bool(int(request.args.get('free', '0')))
    if free_only:
        balloons = client.balloons.get_free()
    else:
        balloons = client.balloons.get_all()

    colors = {balloon.color for balloon in balloons}

    selected_color = request.args.get('color')
    if selected_color:
        balloons = filter_color(balloons, selected_color)

    models = [to_model(balloon, projects) for balloon in balloons]

    return render_template(
        'stock.html',
        title='Balloons',
        free_only=free_only,
        selected_color=selected_color,
        colors=colors,
        balloons=models,
        projects=list(projects.values()),
    )


@stock.post('/search')
def search():
    payload = dict(request.form)

    return redirect(url_for(
        'stock.all_balloons',
        free=int(payload.get('flexRadio') == 'on'),
        color=payload.get('Color'),
    ))


@stock.post('/add_balloon')
def add_balloon():
    payload: dict[str, Any] = dict(request.form)
    payload['uid'] = -1
    payload['acceptance_date'] = datetime.now()
    if payload['project_id'] == '':
        payload['project_id'] = None

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
