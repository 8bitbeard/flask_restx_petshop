"""
User Schema Module
"""

from src.extensions import ma

from src.models.user import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    """
    User Schema Class
    """
    class Meta:
        """
        Meta Class
        """
        model = User
        fields = ("id", "first_name", "last_name", "email")
        ordered = True
