# Estructura inicial del backend

Esta carpeta representa únicamente la organización inicial propuesta en la
arquitectura del proyecto. Todavía no implementa endpoints, base de datos,
autenticación, fuentes externas ni recomendaciones.

```text
backend/
├── app/
│   ├── routes/              # Rutas de la API cuando se defina el framework
│   ├── services/            # Casos de uso y lógica de aplicación
│   ├── models/              # Modelos del dominio
│   ├── database/            # Conexión y persistencia relacional
│   └── recommendations/     # Sistema de recomendaciones
├── tests/                   # Pruebas del backend
├── requirements.txt         # Dependencias, pendientes de selección
└── README.md
```

Python se establece como la tecnología base del backend y se propone utilizar
una base de datos relacional. Las fuentes externas para el catálogo inicial
ya fueron definidas en el SPIKE correspondiente. Todavía están pendientes la
selección del framework específico de Python, el gestor de base de datos y la
definición de los endpoints. Cada parte deberá desarrollarse en una Issue
pequeña, con su rama, pruebas y Pull Request correspondiente.
