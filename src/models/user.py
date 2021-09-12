"""
User Model
"""

import uuid
from datetime import datetime

from src.extensions import db

from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """
    User model class
    """
    __tablename__ = 'users'

    id = db.Column(db.String(100), primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.now())
    updated_at = db.Column(db.DateTime(), onupdate=datetime.now())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if not self.id:
            self.id = str(uuid.uuid4())

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.id)
