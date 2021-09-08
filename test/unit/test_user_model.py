"""
Test file for user model
"""

import pytest

from src.models.user import User


class TestUserModel:
    """
    User Model test class
    """

    def test_new_user(self):
        """
        Tests the creation of a new user
        """
        user = User(first_name='Unit', last_name='Testing', email='unit_testing@example.com', password='123456')
        assert user.id is not None
        assert user.first_name == 'Unit'
        assert user.last_name == 'Testing'
        assert user.email == 'unit_testing@example.com'
        assert user.password_hash is not '123456'

    def test_user_representation(self):
        """
        Tests the user representation
        """
        user = User(first_name='Unit', last_name='Testing', email='unit_testing@example.com', password='123456')
        assert repr(user) == "<User '{}'>".format(user.id)

    def test_user_password_encryption(self):
        """
        Test the user password encryption
        """
        user = User(first_name='Unit', last_name='Testing', email='unit_testing@example.com', password='123456')
        assert user.check_password('123456')

    def test_error_reading_user_password(self):
        """
        Test the user write only password parameter
        """
        user = User(first_name='Unit', last_name='Testing', email='unit_testing@example.com', password='123456')
        with pytest.raises(AttributeError) as execinfo:
            user.password
        assert str(execinfo.value) == 'password: write-only field'
