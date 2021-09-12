"""
Script to create the DB on Docker DB and Heroku
"""

import os

from src import create_app
from src.extensions import db

db.create_all(app=create_app(os.environ['FLASK_ENV']))
