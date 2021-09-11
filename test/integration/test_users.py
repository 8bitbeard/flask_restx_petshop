"""
Users Routes Test File
"""


class TestUsersPost:
    """
    /api/v1/users Test Class
    """

    def test_create_new_user(self, test_client, init_db):
        """
        Test the creation of a new user
        """
        url = '/api/v1/users'
        data = {
            "first_name": "Unit",
            "last_name": "Testing",
            "email": "unit_testing@example.com",
            "password": "123456"
        }
        response = test_client.post(url, json=data)
        assert response.status_code == 201
        assert response.json['id'] is not None
        assert response.json['first_name'] == data['first_name']
        assert response.json['last_name'] == data['last_name']
        assert response.json['email'] == data['email']

    def test_error_register_user_without_first_name(self, test_client, init_db):
        """
        Test the error when trying to register a user without passing the first name parameter
        """
        url = '/api/v1/users'
        data = {
            "last_name": "Testing",
            "email": "unit_testing@example.com",
            "password": "123456"
        }
        response = test_client.post(url, json=data)
        assert response.status_code == 400
        assert response.json['code'] == 'MISSING_PARAMETER'
        assert response.json['message'] == 'Email, First Name, Last Name and Password properties are required!'
        assert response.json['details'] == ['Missing mandatory parameters!']

    def test_error_register_user_without_last_name(self, test_client, init_db):
        """
        Test the error when trying to register a user without passing the last name parameter
        """
        url = '/api/v1/users'
        data = {
            "first_name": "Unit",
            "email": "unit_testing@example.com",
            "password": "123456"
        }
        response = test_client.post(url, json=data)
        assert response.status_code == 400
        assert response.json['code'] == 'MISSING_PARAMETER'
        assert response.json['message'] == 'Email, First Name, Last Name and Password properties are required!'
        assert response.json['details'] == ['Missing mandatory parameters!']

    def test_error_register_user_without_email(self, test_client, init_db):
        """
        Test the error when trying to register a user without passing the email parameter
        """
        url = '/api/v1/users'
        data = {
            "first_name": "Unit",
            "last_name": "Testing",
            "password": "123456"
        }
        response = test_client.post(url, json=data)
        assert response.status_code == 400
        assert response.json['code'] == 'MISSING_PARAMETER'
        assert response.json['message'] == 'Email, First Name, Last Name and Password properties are required!'
        assert response.json['details'] == ['Missing mandatory parameters!']

    def test_error_register_user_without_password(self, test_client, init_db):
        """
        Test the error when trying to register a user without passing the password parameter
        """
        url = '/api/v1/users'
        data = {
            "first_name": "Unit",
            "last_name": "Testing",
            "email": "unit_testing@example.com",
        }
        response = test_client.post(url, json=data)
        assert response.status_code == 400
        assert response.json['code'] == 'MISSING_PARAMETER'
        assert response.json['message'] == 'Email, First Name, Last Name and Password properties are required!'
        assert response.json['details'] == ['Missing mandatory parameters!']

    def test_error_register_user_with_short_first_name(self, test_client, init_db):
        """
        Test the error when trying to register a user with a first name with less than 3 chars
        """
        url = '/api/v1/users'
        data = {
            "first_name": "Un",
            "last_name": "Testing",
            "email": "unit_testing@example.com",
            "password": "123456"
        }
        response = test_client.post(url, json=data)
        assert response.status_code == 400
        assert response.json['code'] == 'INVALID_NAME'
        assert response.json['message'] == 'First Name and Last Name properties must be bigger than 3 chars, be alpahnumeric, also no spaces'
        assert response.json['details'] == ['Provided name is invalid!']

    def test_error_register_user_with_invalid_first_name(self, test_client, init_db):
        """
        Test the error when trying to register a user with a first name containing special chars
        """
        url = '/api/v1/users'
        data = {
            "first_name": "Un%$@",
            "last_name": "Testing",
            "email": "unit_testing@example.com",
            "password": "123456"
        }
        response = test_client.post(url, json=data)
        assert response.status_code == 400
        assert response.json['code'] == 'INVALID_NAME'
        assert response.json['message'] == 'First Name and Last Name properties must be bigger than 3 chars, be alpahnumeric, also no spaces'
        assert response.json['details'] == ['Provided name is invalid!']

    def test_error_register_user_with_short_last_name(self, test_client, init_db):
        """
        Test the error when trying to register a user with a last name with less than 3 chars
        """
        url = '/api/v1/users'
        data = {
            "first_name": "Unit",
            "last_name": "Te",
            "email": "unit_testing@example.com",
            "password": "123456"
        }
        response = test_client.post(url, json=data)
        assert response.status_code == 400
        assert response.json['code'] == 'INVALID_NAME'
        assert response.json['message'] == 'First Name and Last Name properties must be bigger than 3 chars, be alpahnumeric, also no spaces'
        assert response.json['details'] == ['Provided name is invalid!']

    def test_error_register_user_with_invalid_last_name(self, test_client, init_db):
        """
        Test the error when trying to register a user with a last name containing special chars
        """
        url = '/api/v1/users'
        data = {
            "first_name": "Unit",
            "last_name": "Te$$#",
            "email": "unit_testing@example.com",
            "password": "123456"
        }
        response = test_client.post(url, json=data)
        assert response.status_code == 400
        assert response.json['code'] == 'INVALID_NAME'
        assert response.json['message'] == 'First Name and Last Name properties must be bigger than 3 chars, be alpahnumeric, also no spaces'
        assert response.json['details'] == ['Provided name is invalid!']

    def test_error_register_user_with_invalid_email(self, test_client, init_db):
        """
        Test the error when trying to register a user with a invalid email
        """
        url = '/api/v1/users'
        data = {
            "first_name": "Unit",
            "last_name": "Testing",
            "email": "unit_testingexample.com",
            "password": "123456"
        }
        response = test_client.post(url, json=data)
        assert response.status_code == 400
        assert response.json['code'] == 'INVALID_EMAIL'
        assert response.json['message'] == 'The informed Email is not valid!'
        assert response.json['details'] == ['Provided email is invalid!']

    def test_error_register_user_with_short_password(self, test_client, init_db):
        """
        Test the error when trying to register a user with a password that contains less than 6 chars
        """
        url = '/api/v1/users'
        data = {
            "first_name": "Unit",
            "last_name": "Testing",
            "email": "unit_testing@example.com",
            "password": "1234"
        }
        response = test_client.post(url, json=data)
        assert response.status_code == 400
        assert response.json['code'] == 'INVALID_PASSWORD'
        assert response.json['message'] == 'The password must contain 6 or more characters!'
        assert response.json['details'] == ['Provided password is invalid!']

    def test_error_register_user_with_already_taken_email(self, test_client, init_db, insert_user_db):
        """
        Test the error when trying to register a user with an already taken email
        """
        url = '/api/v1/users'
        data = {
            "first_name": "Unit",
            "last_name": "Testing",
            "email": insert_user_db.email,
            "password": "123456"
        }
        response = test_client.post(url, json=data)
        assert response.status_code == 409
        assert response.json['code'] == 'EMAIL_ALREADY_EXISTS'
        assert response.json['message'] == 'The informed Email is already taken!'
        assert response.json['details'] == ['This email is already taken!']