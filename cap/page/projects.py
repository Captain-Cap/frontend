from flask import Blueprint, render_template

from cap.api import client

projects_view = Blueprint('projects', __name__)


@projects_view.get('/')
def start():
    projects = client.projects.get_all()
    return render_template('projects.html', projects=projects)
