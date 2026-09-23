"""
Spike tecnico: FastAPI
Prueba pequena para evaluar FastAPI como framework del backend de RecomendaBook.

Implementa los mismos endpoints que el spike de Flask, para poder comparar
ambas alternativas bajo las mismas condiciones:
- GET /health           -> estado del servicio
- GET /libros           -> listado simple de obras (datos simulados)
- GET /libros/{id}      -> detalle de una obra (datos simulados)
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="RecomendaBook - spike FastAPI")


class Libro(BaseModel):
    id: int
    titulo: str
    tipo: str
    genero: str


LIBROS = [
    Libro(id=1, titulo="Cien anios de soledad", tipo="libro", genero="Realismo magico"),
    Libro(id=2, titulo="Death Note", tipo="manga", genero="Thriller"),
    Libro(id=3, titulo="Watchmen", tipo="comic", genero="Superheroes"),
]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/libros", response_model=list[Libro])
def listar_libros():
    return LIBROS


@app.get("/libros/{libro_id}", response_model=Libro)
def obtener_libro(libro_id: int):
    libro = next((l for l in LIBROS if l.id == libro_id), None)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro
