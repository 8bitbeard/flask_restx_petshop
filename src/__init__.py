import os
from flask import Flask

from src.extensions import db, migrate, bcrypt, ma

from src.config.config import config_by_name

from src.routes import api

basedir = os.path.abspath(os.path.dirname(__file__))
MIGRATION_DIR = os.path.join(basedir, 'database', 'migrations')


def create_app(config_name='development'):

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db, directory=MIGRATION_DIR)

    ma.init_app(app)

    api.init_app(app)

    return app
