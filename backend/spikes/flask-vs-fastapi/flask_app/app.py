"""
Spike tecnico: Flask
Prueba pequena para evaluar Flask como framework del backend de RecomendaBook.

Implementa dos endpoints minimos representativos del sistema:
- GET /health           -> estado del servicio
- GET /libros           -> listado simple de obras (datos simulados)
- GET /libros/<id>      -> detalle de una obra (datos simulados)
"""
from flask import Flask, jsonify, abort

app = Flask(__name__)

LIBROS = [
    {"id": 1, "titulo": "Cien anios de soledad", "tipo": "libro", "genero": "Realismo magico"},
    {"id": 2, "titulo": "Death Note", "tipo": "manga", "genero": "Thriller"},
    {"id": 3, "titulo": "Watchmen", "tipo": "comic", "genero": "Superheroes"},
]


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/libros")
def listar_libros():
    return jsonify(LIBROS)


@app.get("/libros/<int:libro_id>")
def obtener_libro(libro_id):
    libro = next((l for l in LIBROS if l["id"] == libro_id), None)
    if libro is None:
        abort(404, description="Libro no encontrado")
    return jsonify(libro)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
