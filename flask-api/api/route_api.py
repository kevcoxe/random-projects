
from flask import render_template


def load_api(app):
    @app.route('/')
    def index():
        return render_template("index.html")
