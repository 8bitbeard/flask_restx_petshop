from re import DEBUG
import pytest

from src import create_app
from src.extensions import db


@pytest.fixture
def app():
    """
    Instance of Main flask app
    """
    app = create_app(config_name='testing')
    return app


@pytest.fixture
def test_client(app):
    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture
def init_db():
    db.create_all()

    yield db

    db.session.close()
    db.drop_all()


@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock


@pytest.fixture
def mock_db_session(mocker):
    mock = mocker.patch("src.services.users_service.db.session").return_value = mocker.Mock()
    return mock
