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

Las decisiones del framework de Python, gestor de base de datos, endpoints y
fuentes externas siguen pendientes en el RFC. Cada parte deberá desarrollarse
en una Issue pequeña, con su rama, pruebas y Pull Request correspondiente.
