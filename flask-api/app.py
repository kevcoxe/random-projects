
from flask import Flask

from api.route_api import load_api as load_route_api
from api.info_api import load_api as load_info_api


def load_api(app):
    load_route_api(app)
    load_info_api(app)


def run(web_type):
    static_dir = "static"
    template_dir = "templates"

    if web_type == "react":
        static_dir = "../react-web-app/build/static"
        template_dir = "../react-web-app/build"

    app = Flask(
        __name__,
        static_folder=static_dir,
        template_folder=template_dir
    )

    load_api(app)

    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )


if __name__ == '__main__':
    WEB_APP_TYPE = "react"
    run(WEB_APP_TYPE)
