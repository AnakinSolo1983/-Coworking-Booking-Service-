import pytest # import pytest

from fastapi.testclient import TestClient # import TestClient from fastapi.testclient

from app.main import app # import app from app.main


@pytest.fixture # pytest fixture
def client():

    return TestClient(app) # return TestClient