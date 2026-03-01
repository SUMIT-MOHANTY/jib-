import pytest
from unittest.mock import MagicMock, patch
from app import create_app
from app.models.contact import db as _db
from app.models.contact import ContactSubmission
from app.models.projects import Project
from app.models.about import About
from app.models.skills import Skill

@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["WTF_CSRF_ENABLED"] = False
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()

@pytest.fixture(scope="function")
def client(app):
    return app.test_client()

@pytest.fixture(scope="function")
def db(app):
    with app.app_context():
        _db.drop_all()
        _db.create_all()
        yield _db
        _db.session.remove()

@pytest.fixture
def mock_email_service():
    with patch("app.services.email_service.send_notification") as mock:
        mock.return_value = True
        yield mock

@pytest.fixture
def mock_rate_limiter():
    with patch("app.utils.rate_limiter.RateLimiter") as mock:
        instance = MagicMock()
        instance.check_rate_limit.return_value = True
        mock.return_value = instance
        yield instance
