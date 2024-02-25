import pytest
from flask_reports.main import create_app

@pytest.fixture()
def app():
    # Set up all we need for running tests
    app = create_app()

    with app.app_context():
        # Create DB or Update

        # Could return app here, but idea is to yield it
        # Anything before yield = set up
        # Anything after = The teardown for this fixture
        yield app

@pytest.fixture()
# Will run everything in app() then yield, and give us access to all we define there
def client(app):
    # Allow us to simulate requests to app
    return app.test_client()