import os

from flask import Flask

from cap.config import APP_HOST, APP_PORT
from cap.page.home import home
from cap.page.projects import projects
from cap.page.stock import stock

app = Flask(__name__)
app.register_blueprint(home, url_prefix='/')
app.register_blueprint(stock, url_prefix='/stock')
app.register_blueprint(projects, url_prefix='/projects')

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']


if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT)
