from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_responde_ok():
    respuesta = client.get("/health")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"status": "ok"}


def test_cors_permite_al_frontend():
    respuesta = client.get("/health", headers={"Origin": "http://127.0.0.1:8080"})
    assert respuesta.headers["access-control-allow-origin"] == "*"
