from fastapi.testclient import TestClient # import TestClient from fastapi.testclient

from app.main import app # import app from app.main


client = TestClient(app) # create TestClient


# test health:
def test_health():

    response = client.get(
        "/health"
    ) # get health

    assert response.status_code == 200