import pytest
from app import PyFrameApp


@pytest.fixture
def app():
    return PyFrameApp() 

@pytest.fixture
def test_client(app):
    return app.test_session()