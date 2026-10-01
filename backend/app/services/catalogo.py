"""Catalogo de obras.

Por ahora usa datos de ejemplo en memoria. En el Sprint 3 (S3-04/S3-05) se
reemplazara por la base de datos, y en el Sprint 4 por fuentes reales. Las
rutas solo dependen de estas funciones, asi que el cambio no las afecta.
"""
from app.models.libro import Libro

LIBROS = [
    Libro(id=1, titulo="Cien anios de soledad", tipo="libro", genero="Realismo magico", autor="Gabriel Garcia Marquez", calificacion=4.8),
    Libro(id=2, titulo="Death Note", tipo="manga", genero="Thriller", autor="Tsugumi Ohba", calificacion=4.6),
    Libro(id=3, titulo="Watchmen", tipo="comic", genero="Superheroes", autor="Alan Moore", calificacion=4.7),
    Libro(id=4, titulo="El nombre del viento", tipo="libro", genero="Fantasia", autor="Patrick Rothfuss", calificacion=4.5),
    Libro(id=5, titulo="One Piece", tipo="manga", genero="Aventura", autor="Eiichiro Oda", calificacion=4.9),
    Libro(id=6, titulo="Saga", tipo="comic", genero="Ciencia ficcion", autor="Brian K. Vaughan", calificacion=4.4),
]


def listar(tipo: str | None = None) -> list[Libro]:
    """Devuelve el catalogo completo, o filtrado por tipo (libro, manga, comic)."""
    if tipo is None:
        return LIBROS
    return [libro for libro in LIBROS if libro.tipo == tipo]


def obtener(libro_id: int) -> Libro | None:
    """Devuelve una obra por id, o None si no existe."""
    return next((libro for libro in LIBROS if libro.id == libro_id), None)
