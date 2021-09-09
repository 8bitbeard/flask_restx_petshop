"""
Users Service Test File
"""

import pytest
import flask

from src.schemas.user import UserSchema

from src.services.users_service import UsersService
from src.controllers.users_controller import UsersController


class TestPostMethod:
    """
    Users Controller Test Class
    """

    def test_post_controller_method(self, mocker, request_context):
        with request_context():
            request_mock = mocker.patch.object(flask, 'request')
            # request_mock.json.get.return_value = {'first_name': 'Unit', 'last_name': 'Testing',
            #                                       'email': 'unit_testing@example.com', 'password': '123456'}
            # request_mock = mocker.patch('src.controllers.users_controller.request')
            request_mock.json = {'first_name': 'Unit', 'last_name': 'Testing',
                                 'email': 'unit_testing@example.com', 'password': '123456'}
            # service_mock = mocker.patch.object(UsersService, 'create').return_value = mocker.Mock()
            service_mock = mocker.patch('src.controllers.users_controller.UsersService.create')
            service_mock.return_value = mocker.Mock()

            schema_mock = mocker.patch('src.controllers.users_controller.UserSchema.dump')
            schema_mock.return_value = mocker.Mock()

            # schema_mock = mocker.patch.object(UserSchema, 'dump').return_value = mocker.Mock()

            response, status = UsersController.post()

            request_mock.assert_called_once()
            service_mock.assert_called_once()
            schema_mock.assert_called_once()

            # assert response == True
            # assert status == 201
