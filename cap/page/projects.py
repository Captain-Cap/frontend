import os

from flask import Blueprint, render_template

from cap.api.projects import ProjectsApi

projects = Blueprint('projects', __name__)

projapi = ProjectsApi(os.environ['BACKEND_URL'])


@projects.get('/')
def start():
    context = {
        'list_projects': projapi.get_all(),
    }
    return render_template('projects.html', context=context)
