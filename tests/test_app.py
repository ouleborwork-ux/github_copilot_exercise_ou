from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant():
    activity = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/{activity}/participants", params={"email": email})

    assert response.status_code == 200
    assert "removed" in response.json()["message"].lower()
    assert email not in client.get("/activities").json()[activity]["participants"]


def test_unregister_missing_participant_returns_error():
    response = client.delete("/activities/Chess Club/participants", params={"email": "missing@mergington.edu"})

    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
