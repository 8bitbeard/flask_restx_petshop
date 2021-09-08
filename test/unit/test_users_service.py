"""
Users Service Test File
"""

import pytest

from src.services.users_service import UsersService
from src.exceptions.user_exceptions import UserMissingParameter, UserNameInvalid, UserEmailInvalid, \
                                           UserEmailAlreadyExists, UserPasswordTooShort


class TestCreateMethod:
    """
    Users Service Test Class
    """

    def test_error_create_user_without_first_name(self):
        """
        Test if service create method raises an error when trying to create a user without first name
        """
        users_service = UsersService()
        with pytest.raises(UserMissingParameter) as execinfo:
            users_service.create({'last_name': 'Testing', 'email': 'unit_testing@example.com', 'password': '123456'})
        assert str(execinfo.value) == 'Email, First Name, Last Name and Password properties are required!'

    def test_error_create_user_without_last_name(self):
        """
        Test if service create method raises an error when trying to create a user without last name
        """
        users_service = UsersService()
        with pytest.raises(UserMissingParameter) as execinfo:
            users_service.create({'first_name': 'Unit', 'email': 'unit_testing@example.com', 'password': '123456'})
        assert str(execinfo.value) == 'Email, First Name, Last Name and Password properties are required!'

    def test_error_create_user_without_email(self):
        """
        Test if service create method raises an error when trying to create a user without email
        """
        users_service = UsersService()
        with pytest.raises(UserMissingParameter) as execinfo:
            users_service.create({'first_name': 'Unit', 'last_name': 'Testing', 'password': '123456'})
        assert str(execinfo.value) == 'Email, First Name, Last Name and Password properties are required!'

    def test_error_create_user_without_password(self):
        """
        Test if service create method raises an error when trying to create a user without password
        """
        users_service = UsersService()
        with pytest.raises(UserMissingParameter) as execinfo:
            users_service.create({'first_name': 'Unit', 'last_name': 'Testing', 'email': 'unit_testing@example.com'})
        assert str(execinfo.value) == 'Email, First Name, Last Name and Password properties are required!'

    def test_error_create_user_with_less_than_3_first_name_chars(self):
        """
        Test if service create method raises an error when trying to create a user with first name lass than 3 chars
        """
        users_service = UsersService()
        with pytest.raises(UserNameInvalid) as execinfo:
            users_service.create(
                {
                    'first_name': 'U',
                    'last_name': 'Testing',
                    'email': 'unit_testing@example.com',
                    'password': '123456'
                }
            )
        assert str(execinfo.value) == 'First Name and Last Name properties must be bigger than 3 chars, be alpahnumeric, also no spaces'

    def test_error_create_user_with_less_than_3_last_name_chars(self):
        """
        Test if service create method raises an error when trying to create a user with last name lass than 3 chars
        """
        users_service = UsersService()
        with pytest.raises(UserNameInvalid) as exception:
            users_service.create(
                {
                    'first_name': 'Unit',
                    'last_name': 'Te',
                    'email': 'unit_testing@example.com',
                    'password': '123456'
                }
            )
        assert str(exception.value) == 'First Name and Last Name properties must be bigger than 3 chars, be alpahnumeric, also no spaces'

    def test_error_create_user_first_name_not_alphanumeric(self):
        """
        Test if service create method raises an error when trying to create a user with a non alphanumeric first name
        """
        users_service = UsersService()
        with pytest.raises(UserNameInvalid) as exception:
            users_service.create({'first_name': 'Un$t', 'last_name': 'Test',
                                  'email': 'unit_testing@example.com', 'password': '123456'})
        assert str(exception.value) == 'First Name and Last Name properties must be bigger than 3 chars, be alpahnumeric, also no spaces'

    def test_error_create_user_last_name_not_alphanumeric(self):
        """
        Test if service create method raises an error when trying to create a user with a non alphanumeric first name
        """
        users_service = UsersService()
        with pytest.raises(UserNameInvalid) as exception:
            users_service.create({'first_name': 'Unit', 'last_name': 'T3$t',
                                  'email': 'unit_testing@example.com', 'password': '123456'})
        assert str(exception.value) == 'First Name and Last Name properties must be bigger than 3 chars, be alpahnumeric, also no spaces'

    def test_error_create_user_with_invalid_email(self):
        """
        Test if service create method raises an error when trying to create a user with an invalid email
        """
        users_service = UsersService()
        with pytest.raises(UserEmailInvalid) as exception:
            users_service.create({'first_name': 'Unit', 'last_name': 'Test',
                                  'email': 'unit_testingexample.com', 'password': '123456'})
        assert str(exception.value) == 'The informed Email is not valid!'

    def test_error_create_user_with_invalid_password(self):
        """
        Test if service create method raises an error when trying to create a user with an invalid password
        """
        users_service = UsersService()
        with pytest.raises(UserPasswordTooShort) as exception:
            users_service.create({'first_name': 'Unit', 'last_name': 'Test',
                                  'email': 'unit_testing@example.com', 'password': '123'})
        assert str(exception.value) == 'The password must contain 6 or more characters!'

    def test_error_create_user_with_already_taken_email(self, mock_get_sqlalchemy):
        """
        Test if service create method raises an error when trying to create a user with an already taken email
        """
        mock_get_sqlalchemy.filter_by.return_value.first.return_value = True
        users_service = UsersService()
        with pytest.raises(UserEmailAlreadyExists) as exception:
            users_service.create({'first_name': 'Unit', 'last_name': 'Test',
                                  'email': 'unit_testing@example.com', 'password': '123456'})
        assert str(exception.value) == 'The informed Email is already taken!'

    def test_create_user_service_method(self, mock_get_sqlalchemy, mock_db_session):
        """
        Test if create method registers a new user successfully
        """
        mock_get_sqlalchemy.filter_by.return_value.first.return_value = None
        users_service = UsersService()
        user = users_service.create({'first_name': 'Unit', 'last_name': 'Test',
                                     'email': 'unit_testing@example.com', 'password': '123456'})
        assert user.id is not None
        assert user.first_name == 'Unit'
        assert user.last_name == 'Test'
        assert user.email == 'unit_testing@example.com'
        assert user.password_hash is not None
        assert user.check_password('123456') is True

