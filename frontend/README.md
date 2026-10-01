# Frontend de RecomendaBook

Aplicacion web responsive con HTML, CSS y JavaScript puro (sin frameworks, como se propone en el RFC).
Por ahora muestra el catalogo de obras (libros, manga y comics) y permite filtrarlo por tipo.
Consume la API del backend en `http://127.0.0.1:8000`.

```text
frontend/
├── index.html        # Punto de entrada de la interfaz
├── css/
│   └── styles.css    # Estilos y diseno responsive
├── js/
│   └── main.js       # Consulta la API (GET /libros) y pinta el catalogo
└── README.md
```

## Como correrlo

1. Levantar el backend (desde la carpeta `backend/`):

   ```bash
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

2. Levantar el frontend (desde la carpeta `frontend/`), en otra terminal:

   ```bash
   python -m http.server 8080
   ```

3. Abrir http://127.0.0.1:8080 en el navegador.

Si cambias el puerto o la direccion del backend, ajusta la constante `API_URL` al inicio de `js/main.js`.

Las demas pantallas (busqueda, autenticacion, detalle, valoraciones y recomendaciones) se desarrollaran en Issues posteriores, una funcionalidad a la vez, con sus pruebas y Pull Requests.
