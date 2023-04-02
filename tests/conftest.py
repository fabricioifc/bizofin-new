import pytest
from app import create_app
from app.extensions import db

@pytest.fixture()
def app():
  # Create a Flask app configured for testing
  app = create_app('config.TestingConfig')

  with app.app_context():
    db.drop_all()
    db.create_all()
    yield app  # this is where the testing happens!

@pytest.fixture()
def client(app):
  return app.test_client()