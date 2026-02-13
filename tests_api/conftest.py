import pytest
from api.api_client import APIClient
from db_client import DBClient

@pytest.fixture
def api():
    return APIClient()

@pytest.fixture(scope="session")
def db():
    client = DBClient()
    yield client
    client.close()
