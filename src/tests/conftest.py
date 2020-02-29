import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture
def client(socket_enabled):
    with TestClient(app) as client:
        yield client
