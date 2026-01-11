

# Arquitectura del proyecto gestion_web , es base para ampliarla

## Estructura general

gestion_web/
├── gestion/              # Proyecto Django (settings, urls, wsgi)
├── personas/             # App personas (CRUD)
├── usuarios/             # App usuarios (CRUD)
├── templates/
│   ├── base.html         # Layout global (menú unificado)
│   ├── inicio.html
│   ├── personas/
│   └── usuarios/
├── static/
│   └── css/js/img
├── db.sqlite3
└── manage.py

## Convenciones del proyecto

- Cada módulo es una app Django independiente.
- Todas las vistas renderizan templates (no HttpResponse directo).
- Todos los templates heredan de base.html.
- El menú de navegación vive solo en base.html.
- URLs de cada módulo están bajo su prefijo (/personas/, /usuarios/).
- CRUD completo por módulo.
- SQLite para desarrollo, MySQL en producción.
- No se usan librerías externas innecesarias.
