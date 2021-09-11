import os
from flask import Flask
from flask.json import jsonify

from src.extensions import db, migrate, ma

from src.config.config import config_by_name

from src.routes import api

from src.exceptions import APIError

basedir = os.path.abspath(os.path.dirname(__file__))
MIGRATION_DIR = os.path.join(basedir, 'database', 'migrations')


def create_app(config_name='development'):

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    migrate.init_app(app, db, directory=MIGRATION_DIR)

    ma.init_app(app)

    api.init_app(app)

    @app.errorhandler(APIError)
    def handle_exception(err):
        """Return custom JSON when APIError or its children are raised"""
        response = {
            "code": err.code,
            "message": "",
            "details": [
                err.details
            ]
        }
        if len(err.args) > 0:
            response["message"] = err.args[0]
        return jsonify(response), err.status_code

    return app
