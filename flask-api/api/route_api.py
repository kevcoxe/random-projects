
import os
from flask import render_template


def load_api(app):
    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/faces')
    def faces():

        faces = []
        for (dirpath, dirnames, filenames) in os.walk('static/images'):
            for filename in filenames:
                faces.append({'src': 'static/images/{}'.format(filename)})

        return render_template("faces.html", faces=faces)
