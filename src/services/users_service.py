"""
Users Service Module
"""
import validators
from src.extensions import db

from src.models.user import User

from src.exceptions.user_exceptions import UserMissingParameter, UserNameInvalid, UserEmailInvalid,\
                                           UserEmailAlreadyExists, UserPasswordTooShort


class UsersService:
    """
    Users Service Class
    """

    @staticmethod
    def create(data):

        if 'email' not in data or 'first_name' not in data or 'last_name' not in data or 'password' not in data:
            raise UserMissingParameter('Email, First Name, Last Name and Password properties are required!')

        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']

        if len(first_name) < 3 or not first_name.isalnum() or len(last_name) < 3 or not last_name.isalnum():
            raise UserNameInvalid(
                'First Name and Last Name properties must be bigger than 3 chars, be alpahnumeric, also no spaces'
            )

        if not validators.email(email):
            raise UserEmailInvalid('The informed Email is not valid!')

        if len(password) < 6:
            raise UserPasswordTooShort('The password must contain 6 or more characters!')

        found_user = User.query.filter_by(email=email).first()

        if found_user:
            raise UserEmailAlreadyExists('The informed Email is already taken!')

        user = User(first_name=first_name, last_name=last_name, email=email, password=password)

        db.session.add(user)
        db.session.commit()

        return user
