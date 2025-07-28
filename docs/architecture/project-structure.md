# 📂 Estructura del Proyecto

El proyecto está organizado siguiendo las mejores prácticas para una aplicación FastAPI, promoviendo la separación de responsabilidades.

```
.
├── README.md
├── app/
│   ├── api/
│   │   ├── api.py
│   │   └── endpoints/
│   │       ├── general.py
│   │       └── users.py
│   ├── core/
│   │   └── config.py
│   ├── main.py
│   ├── schemas/
│   │   ├── album.py
│   │   ├── post.py
│   │   ├── response.py
│   │   ├── todos.py
│   │   └── user.py
│   ├── services/
│   │   └── external_api_service.py
│   └── utils/
│       ├── api_error_handler.py
│       └── logger_config.py
├── main.py
├── poetry.lock
├── pyproject.toml
└── tests/
    ├── data.py
    ├── test_endpoint.py
    └── test_service.py
```


### Descripción de Componentes

*   **`app/`**: Directorio principal que contiene todo el código fuente de la aplicación.
    *   **`api/`**: Módulo que define todos los endpoints de la API.
        *   `api.py`: Integra todos los routers de los endpoints en un único `APIRouter` principal.
        *   `endpoints/`: Contiene los endpoints agrupados por recurso para mayor claridad (`general.py`, `users.py`).
    *   **`core/`**: Se encarga de la configuración central del proyecto.
        *   `config.py`: Carga y gestiona las variables de entorno usando `pydantic-settings`.
    *   **`main.py` (dentro de `app/`)**: Punto de entrada de la aplicación. Aquí se crea la instancia principal de `FastAPI` y se incluye el router de la API.
    *   **`schemas/`**: Contiene todos los modelos de datos de Pydantic utilizados para la validación, serialización y documentación de la API.
    *   **`services/`**: Encapsula la lógica de negocio y la comunicación con servicios externos.
        *   `external_api_service.py`: Clase responsable de toda la comunicación con la API de JSONPlaceholder.
    *   **`utils/`**: Alberga funciones y utilidades reutilizables.
        *   `api_error_handler.py`: Decorador para el manejo centralizado y consistente de excepciones.
        *   `logger_config.py`: Configuración del sistema de `logging` de la aplicación.
*   **`main.py` (en la raíz)**: Script de conveniencia para ejecutar la aplicación con `uvicorn` de forma programática, útil para ciertos entornos de despliegue o para facilitar el arranque (`python main.py`).
*   **`pyproject.toml`**: Archivo de configuración para Poetry. Define las dependencias del proyecto, metadatos y scripts.
*   **`tests/`**: Directorio que contiene todas las pruebas automatizadas.
    *   `test_service.py`: Pruebas unitarias para la capa de servicios, simulando la red con `respx`.
    *   `test_endpoint.py`: Pruebas de integración para la capa de la API, simulando la capa de servicios con `unittest.mock` y `dependency_overrides` de FastAPI.