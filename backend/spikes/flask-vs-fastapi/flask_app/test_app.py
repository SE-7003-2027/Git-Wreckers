from app import app


def client():
    app.testing = True
    return app.test_client()


def test_health():
    resp = client().get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_listar_libros():
    resp = client().get("/libros")
    assert resp.status_code == 200
    data = resp.get_json()
    assert len(data) == 3
    assert data[0]["titulo"] == "Cien anios de soledad"


def test_obtener_libro_existente():
    resp = client().get("/libros/2")
    assert resp.status_code == 200
    assert resp.get_json()["titulo"] == "Death Note"


def test_obtener_libro_inexistente():
    resp = client().get("/libros/999")
    assert resp.status_code == 404
