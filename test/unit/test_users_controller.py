"""
Users Service Test File
"""

import pytest

from src.controllers.users_controller import UsersController


class TestPostMethod:
    """
    Users Controller Test Class
    """


    @pytest.mark.asyncio
    async def test_post_controller_method(self, mocker, request_context):
        with request_context():
            request_mock = mocker.patch('src.controllers.users_controller.request').return_value = mocker.MagicMock()
            request_mock.return_value.get_json.return_value = mocker.Mock()
            service_mock = mocker.patch('src.controllers.users_controller.UsersService')
            service_mock.create.return_value = mocker.Mock()
            schema_mock = mocker.patch('src.controllers.users_controller.UserSchema')
            schema_mock.dump.return_value = mocker.Mock()

            await UsersController.post()

        request_mock.get_json.assert_called_once()
        service_mock.assert_called_once()
        schema_mock.assert_called_once()
