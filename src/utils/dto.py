from flask_restx import Namespace, fields


class UserDto:

    api = Namespace("user", description="User related operations.")
    user = api.model(
        "User object",
        {
            "email": fields.String(required=True, descrption='User email address'),
            "first_name": fields.String(required=True, description='User first name'),
            "last_name": fields.String(required=True, description='User last name'),
            "password": fields.String(required=True, description='User password')
        },
    )

    data_resp = api.model(
        "User Data Response",
        {
            "user": fields.Nested(user),
        },
    )
