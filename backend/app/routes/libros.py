"""Rutas del catalogo de obras."""
from fastapi import APIRouter, HTTPException

from app.models.libro import Libro
from app.services import catalogo

router = APIRouter(prefix="/libros", tags=["libros"])


@router.get("", response_model=list[Libro])
def listar_libros(tipo: str | None = None):
    """Lista las obras, con filtro opcional por tipo (libro, manga, comic)."""
    return catalogo.listar(tipo)


@router.get("/{libro_id}", response_model=Libro)
def obtener_libro(libro_id: int):
    """Devuelve el detalle de una obra."""
    libro = catalogo.obtener(libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro
