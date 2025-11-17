from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_predict_valid():
    response = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 200
    assert "predicted_class" in response.json()


def test_predict_invalid_length():
    response = client.post("/predict", json={"features": [1.0, 2.0]})
    assert response.status_code == 400
