from flask import Blueprint, render_template

index = Blueprint('index', __name__)


@index.get('/')
def start():
    context = {
        'title_project': 'Captain Cap',
    }
    return render_template('index.html', context=context)
