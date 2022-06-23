from flask import Blueprint, render_template

from cap.api.projects import ProjectsApi
from cap.config import config

projects = Blueprint('projects', __name__)

projapi = ProjectsApi(config.url)


@projects.get('/')
def start():
    context = {
        'list_projects': projapi.get_all(),
    }
    return render_template('projects.html', context=context)
