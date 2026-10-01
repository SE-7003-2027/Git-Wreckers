from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_listar_libros_devuelve_el_catalogo():
    respuesta = client.get("/libros")
    assert respuesta.status_code == 200
    libros = respuesta.json()
    assert len(libros) == 6
    assert {"id", "titulo", "tipo", "genero", "autor", "calificacion"} <= set(libros[0])


def test_filtrar_por_tipo():
    respuesta = client.get("/libros", params={"tipo": "manga"})
    assert respuesta.status_code == 200
    titulos = [libro["titulo"] for libro in respuesta.json()]
    assert titulos == ["Death Note", "One Piece"]


def test_filtrar_por_tipo_sin_resultados():
    respuesta = client.get("/libros", params={"tipo": "revista"})
    assert respuesta.status_code == 200
    assert respuesta.json() == []


def test_obtener_libro_existente():
    respuesta = client.get("/libros/3")
    assert respuesta.status_code == 200
    assert respuesta.json()["titulo"] == "Watchmen"


def test_obtener_libro_inexistente_devuelve_404():
    respuesta = client.get("/libros/999")
    assert respuesta.status_code == 404
    assert respuesta.json()["detail"] == "Libro no encontrado"


def test_id_invalido_devuelve_422():
    respuesta = client.get("/libros/abc")
    assert respuesta.status_code == 422
