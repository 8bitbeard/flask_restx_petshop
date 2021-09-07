from flask_restx import Api

from src.controllers.users_controller import UsersController

api = Api(
    version='1.0',
    title='Flask RESTx Petshop',
    description='Simple Petshop API developed with Flask RESTx',
    prefix='/api/v1'
)

api.add_resource(UsersController, '/users')
