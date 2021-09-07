"""
Users Controller Module
"""
from flask import request
from flask_restx import Resource

from src.services.users_service import UsersService

from src.utils.dto import UserDto

from src.schemas.user import UserSchema

api = UserDto.api
user = UserDto.user


class UsersController(Resource):

    @staticmethod
    def post():
        data = request.json

        users_service = UsersService()
        user_schema = UserSchema()

        created_user = users_service.create(data)

        return user_schema.dump(created_user), 201
