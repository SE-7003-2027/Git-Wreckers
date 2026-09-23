# Demo funcional de RecomendaBook

Pagina web funcional, de principio a fin, para mostrar en la presentacion del equipo: un frontend que consulta un backend real y muestra el catalogo de libros, comics y manga con filtros por tipo.

Sigue la arquitectura propuesta en el RFC: frontend en HTML/CSS/JS y backend en Python con FastAPI.

## Como correrlo

1. Backend (en una terminal):

```
cd demo/backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Esto levanta el servidor en http://127.0.0.1:8000

2. Frontend (en otra terminal):

```
cd demo/frontend
python -m http.server 8080
```

Y abrir http://127.0.0.1:8080 en el navegador.

## Que incluye

Backend (`demo/backend/main.py`): expone `/libros` (con filtro opcional `?tipo=`) y `/libros/{id}`, con datos de ejemplo de libros, comics y manga.

Frontend (`demo/frontend/`): pagina que consulta el backend y muestra el catalogo en tarjetas, con botones para filtrar por tipo de obra.

## Notas

Los datos son de ejemplo (no vienen de una base de datos ni de una fuente externa todavia), pero la conexion frontend-backend es real: si cambias los datos en el backend, se reflejan en la pagina.

Este demo es una base para ir conectando las funcionalidades reales del PRD (busqueda, calificaciones, recomendaciones) conforme se vayan implementando.
