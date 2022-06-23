from flask import Blueprint, render_template

home = Blueprint('home', __name__)


@home.get('/')
def start():
    context = {
        'title_project': 'Captain Cap',
    }
    return render_template('home.html', context=context)
