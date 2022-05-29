from distutils.log import debug
from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def index():
    name_project = 'Captain Cap'
    return render_template('index.html', title_project=name_project)


if __name__ == "__main__":
    app.run(debug=True)