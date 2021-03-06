from datetime import datetime
from typing import Any

from flask import Blueprint, redirect, render_template, request, url_for

from cap.api import client
from cap.api.schemas import ProjectsModel

projects_view = Blueprint('projects', __name__)


@projects_view.get('/')
def all_projects():
    projects = client.projects.get_all()
    return render_template('projects.html', projects=projects)


@projects_view.get('/more/<int:uid>')
def details(uid):
    name = request.args['name']
    balloon_project = client.projects.get_for_project(uid)
    return render_template(
        'more_projects.html',
        balloons=balloon_project,
        project_name=name,
    )


@projects_view.get('/edit/<int:uid>')
def edit_page(uid):
    project = client.projects.get_by_id(uid)
    return render_template('projects_edit.html', project=project)


@projects_view.post('/edit/<int:uid>')
def edit(uid):
    payload: dict[str, Any] = dict(request.form)
    payload['uid'] = uid
    project = ProjectsModel(**payload)
    client.projects.update(project)
    return redirect(url_for('projects.all_projects'))


@projects_view.post('/add')
def add():
    payload: dict[str, Any] = dict(request.form)
    payload['uid'] = -1
    payload['created_at'] = datetime.now()

    project = ProjectsModel(**payload)
    client.projects.add(project)
    return redirect(url_for('projects.all_projects'))


@projects_view.get('/delete_page/<int:uid>')
def delete_page(uid):
    return render_template('delete_project.html', uid=uid)


@projects_view.get('/delete/<int:uid>')
def delete(uid):
    client.projects.delete(uid)
    return redirect(url_for('projects.all_projects'))
