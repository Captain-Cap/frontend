from flask import Flask, render_template

from cap.api.balloons import BalloonApi

app = Flask(__name__)
balloon = BalloonApi()


@app.route('/')
def index():
    context = {
        'title_project': 'Captain Cap',
    }
    return render_template('index.html', context=context)


@app.route('/balloons')
def balloons():
    context = {
        'title': 'Balloons',
        'list_balloons': balloon.get_all(),
    }
    return render_template('balloons.html', context=context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
