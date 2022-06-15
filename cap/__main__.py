import os

from flask import Flask

from cap.page.index import index
from cap.page.stock import stock

app = Flask(__name__)
app.register_blueprint(index, url_prefix='/')
app.register_blueprint(stock, url_prefix='/stock/')

host_local = os.environ['HOST_LOCAL']
port_local = int(os.environ['PORT_LOCAL'])

SECRET_KEY = os.environ['SECRET_KEY']
app.config['SECRET_KEY'] = SECRET_KEY


if __name__ == '__main__':
    app.run(host_local, port_local)
