"""Punto de entrada del backend de RecomendaBook.

Como correrlo (desde la carpeta backend/):
    pip install -r requirements.txt
    uvicorn app.main:app --reload

Esto levanta el servidor en http://127.0.0.1:8000
La documentacion interactiva queda en http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import libros

app = FastAPI(title="RecomendaBook")

# Permite que el frontend (servido en otro puerto) consulte la API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(libros.router)


@app.get("/health")
def health():
    """Estado del servicio."""
    return {"status": "ok"}
