"""
Extensions initialization module

When app is created, each extension is initialized
"""


from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
ma = Marshmallow()
