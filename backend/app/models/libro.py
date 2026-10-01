"""Modelo de dominio de una obra (libro, comic o manga)."""
from pydantic import BaseModel


class Libro(BaseModel):
    id: int
    titulo: str
    tipo: str
    genero: str
    autor: str
    calificacion: float
