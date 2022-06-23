import os

from flask import Flask

from cap.config import config
from cap.page.home import home
from cap.page.projects import projects
from cap.page.stock import stock

app = Flask(__name__)
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(stock, url_prefix='/stock')
app.register_blueprint(projects, url_prefix='/projects')

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']


if __name__ == '__main__':
    app.run(host=config.app_host, port=config.app_port)
