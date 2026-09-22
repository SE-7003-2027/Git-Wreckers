"""
Demo funcional de RecomendaBook (backend)

Pequeno servidor con FastAPI que expone el catalogo de libros/comics/manga
de prueba, para que el frontend pueda consumirlo y mostrar algo funcional
de principio a fin en la presentacion del equipo.

Como correrlo:
    pip install -r requirements.txt
    uvicorn main:app --reload

Esto levanta el servidor en http://127.0.0.1:8000
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="RecomendaBook - demo funcional")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Libro(BaseModel):
    id: int
    titulo: str
    tipo: str
    genero: str
    autor: str
    calificacion: float

LIBROS = [
    Libro(id=1, titulo="Cien anios de soledad", tipo="libro", genero="Realismo magico", autor="Gabriel Garcia Marquez", calificacion=4.8),
    Libro(id=2, titulo="Death Note", tipo="manga", genero="Thriller", autor="Tsugumi Ohba", calificacion=4.6),
    Libro(id=3, titulo="Watchmen", tipo="comic", genero="Superheroes", autor="Alan Moore", calificacion=4.7),
    Libro(id=4, titulo="El nombre del viento", tipo="libro", genero="Fantasia", autor="Patrick Rothfuss", calificacion=4.5),
    Libro(id=5, titulo="One Piece", tipo="manga", genero="Aventura", autor="Eiichiro Oda", calificacion=4.9),
    Libro(id=6, titulo="Saga", tipo="comic", genero="Ciencia ficcion", autor="Brian K. Vaughan", calificacion=4.4),
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/libros", response_model=list[Libro])
def listar_libros(tipo: str | None = None):
    """Devuelve el catalogo completo, o filtrado por tipo (libro, manga, comic)."""
    if tipo is None:
        return LIBROS
    return [l for l in LIBROS if l.tipo == tipo]

@app.get("/libros/{libro_id}", response_model=Libro)
def obtener_libro(libro_id: int):
    libro = next((l for l in LIBROS if l.id == libro_id), None)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro
