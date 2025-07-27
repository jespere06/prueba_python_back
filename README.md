
# API Proxy para JSONPlaceholder

_Un servicio backend robusto construido con FastAPI y Python como parte de una prueba técnica._

[![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1+-darkgreen?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Poetry](https://img.shields.io/badge/Poetry-1.8.2-blueviolet?logo=poetry)](https://python-poetry.org/)
[![Pytest](https://img.shields.io/badge/Pytest-8.4.1+-blue?logo=pytest)](https://pytest.org/)

---

## 📜 Tabla de Contenidos

1.  [Descripción del Proyecto](#-descripción-del-proyecto)
2.  [✨ Características Principales](#-características-principales)
3.  [📂 Estructura del Proyecto](#-estructura-del-proyecto)
4.  [⚙️ Requisitos Previos](#️-requisitos-previos)
5.  [🚀 Guía de Instalación y Ejecución](#-guía-de-instalación-y-ejecución)
6.  [🔌 Uso de la API](#-uso-de-la-api)
7.  [🧪 Ejecución de Pruebas](#-ejecución-de-pruebas)
8.  [💡 Decisiones de Diseño](#-decisiones-de-diseño)

## 📝 Descripción del Proyecto

Este proyecto consiste en una API RESTful que actúa como un proxy o *wrapper* para la API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/). Fue desarrollado como parte de una prueba técnica para demostrar competencias en el desarrollo de servicios backend utilizando Python y FastAPI.

La API no solo reexpone los datos de JSONPlaceholder, sino que añade una capa de valor al:
*   **Estructurar las respuestas** en un formato consistente y predecible.
*   **Validar los datos** de entrada y salida mediante modelos Pydantic.
*   **Enriquecer las respuestas** con metadatos útiles, como un `timestamp`.

El código sigue los principios de **Arquitectura Limpia**, garantizando que sea mantenible, escalable y fácil de testear.

## ✨ Características Principales

*   **⚡ API Asíncrona de Alto Rendimiento:** Construida sobre FastAPI y `httpx`, aprovechando la concurrencia de Python para un manejo de E/S no bloqueante y eficiente.
*   **🏛️ Arquitectura Limpia:** Separación clara de responsabilidades en capas (API, Servicios, Esquemas) para facilitar el mantenimiento, la escalabilidad y las pruebas.
*   **🛡️ Validación de Datos Robusta:** Uso intensivo de modelos Pydantic para validar, serializar y documentar automáticamente los datos de entrada y salida, garantizando la integridad de los datos.
*   **📦 Gestión de Dependencias Moderna:** Uso de [Poetry](https://python-poetry.org/) para una gestión de dependencias y entornos virtuales determinista y reproducible.
*   **✅ Suite de Pruebas Completa:** Pruebas unitarias y de integración con `pytest`. Se utiliza `respx` para simular las llamadas a la API externa y el sistema de inyección de dependencias de FastAPI para aislar componentes, garantizando la fiabilidad del código.
*   **Estratégia de Manejo de Errores Centralizada:** Un decorador personalizado (`@handle_api_error`) gestiona las excepciones de forma consistente en toda la API, devolviendo respuestas de error claras y estandarizadas.
*   **📝 Logging Configurado:** Sistema de registro de eventos importantes y errores para facilitar la depuración y monitorización en entornos de producción.
*   **📚 Documentación Automática:** Gracias a FastAPI, la API se autodocumenta. Se generan interfaces interactivas con Swagger UI y ReDoc sin esfuerzo adicional.

## 📂 Estructura del Proyecto

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

## ⚙️ Requisitos Previos

Asegúrate de tener instalado el siguiente software en tu sistema:

*   **Python 3.13+**
*   **Poetry**

## 🚀 Guía de Instalación y Ejecución

Sigue estos pasos para poner en marcha el proyecto en tu entorno local.

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/jespere06/prueba_python_back
    cd prueba_python_back
    ```

2.  **Crear el archivo de entorno `.env`:**
    Crea este archivo en la raíz del proyecto con el siguiente contenido:
    ```env
    PROJECT_NAME="JSONPlaceholder API Proxy"
    JSONPLACEHOLDER_BASE_URL="https://jsonplaceholder.typicode.com"
    VERSION="1.0.0"
    ```

3.  **Instalar dependencias con Poetry:**
    Este comando creará un entorno virtual y instalará todas las dependencias definidas en `pyproject.toml`.
    ```bash
    poetry install
    ```

4.  **Activar el entorno virtual:**
    Para trabajar con las dependencias instaladas, debes activar el entorno virtual. Este comando lo hace en tu sesión de terminal actual:

    **En macOS / Linux:**
    ```bash
    source $(poetry env info --path)/bin/activate
    ```
    *(**Nota:** Este método es preferible a `poetry shell` para scripts o cuando se desea mantener la sesión de shell actual).*

    **En Windows (PowerShell):**
    ```powershell
    # Primero, obtén la ruta del entorno
    $VENV_PATH = poetry env info --path
    # Luego, usa la ruta para ejecutar el script de activación
    & "$VENV_PATH\Scripts\activate.ps1"
    ```

5.  **Iniciar el servidor de desarrollo:**
    Una vez activado el entorno, usa `uvicorn` para iniciar la aplicación. El flag `--reload` reiniciará el servidor automáticamente tras cada cambio en el código.
    ```bash
    uvicorn app.main:app --reload
    ```

6.  **¡Listo!**
    La API estará disponible en `http://127.0.0.1:8000`.

## 🔌 Uso de la API

### Documentación Interactiva

La forma más sencilla de explorar y probar la API es a través de la documentación autogenerada por FastAPI, que proporciona una interfaz interactiva para cada endpoint:

*   **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
*   **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### Ejemplos con `curl`

A continuación se muestran ejemplos detallados para cada endpoint, incluyendo casos de éxito y de error.

> [!TIP]
> Para formatear la salida JSON y hacerla más legible en la terminal, puedes añadir `| jq` al final de tus comandos `curl`.

#### 1. Endpoint Raíz (`GET /`)
Obtiene información básica sobre la API.

```bash
curl -X GET "http://127.0.0.1:8000/"
```

**Respuesta Exitosa (200 OK):**
```json
{
  "timestamp": "2025-07-27 16:56:43",
  "body": {
    "message": "Bienvenido a la API de base de datos de JSONPlaceholder.",
    "name": "JSONPlaceholder API",
    "description": "",
    "version": "1.0.0"
  }
}
```

#### 2. Verificación de Estado (`GET /health`)
Comprueba si el servicio está operativo.

```bash
curl -X GET "http://127.0.0.1:8000/health"
```

**Respuesta Exitosa (200 OK):**
```json
{
  "timestamp": "2025-07-27 16:57:00",
  "body": {
    "status": "ok"
  }
}
```

#### 3. Obtener Información de un Usuario (`GET /users/{id}`)
Este endpoint utiliza un **parámetro de ruta** (`path parameter`).

*   **Caso de Éxito (Usuario existente):**
    ```bash
    curl -X GET "http://127.0.0.1:8000/users/1"
    ```
*   **Caso de Error (Usuario no encontrado):**
    ```bash
    curl -X GET "http://127.0.0.1:8000/users/999"
    ```
    **Respuesta de Error (404 Not Found):**
    ```json
    {
      "detail": "El Usuario con el ID 999 no ha sido encontrado"
    }
    ```

#### 4. Endpoints con Parámetro de Consulta (`?id=...`)
Los siguientes endpoints (`/posts`, `/albums`, `/todos`) utilizan un **parámetro de consulta** (`query parameter`) obligatorio para identificar al usuario.

##### `GET /posts?id={user_id}`

*   **Caso de Éxito (Usuario con posts):**
    ```bash
    curl -X GET "http://127.0.0.1:8000/posts?id=1"
    ```
    **Respuesta Exitosa (200 OK):** (respuesta truncada para legibilidad)
    ```json
    {
      "timestamp": "2025-07-27 16:58:11",
      "body": [
        {
          "user_id": 1,
          "post_id": 1,
          "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
          "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        },
        {
          "user_id": 1,
          "post_id": 2,
          "title": "qui est esse",
          "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
        }
      ]
    }
    ```

*   **Error de Validación (Parámetro `id` faltante):**
    ```bash
    curl -X GET "http://127.0.0.1:8000/posts"
    ```
    **Respuesta de Error (422 Unprocessable Entity):**
    ```json
    {
      "detail": [
        { "type": "missing", "loc": ["query", "id"], "msg": "Field required", "input": null }
      ]
    }
    ```

*   **Error Lógico (Usuario no existe):**
    ```bash
    curl -X GET "http://127.0.0.1:8000/posts?id=-3"
    ```
    **Respuesta de Error (404 Not Found):**
    ```json
    {
      "detail": "El Usuario con el ID -3 no ha sido encontrado"
    }
    ```

##### `GET /albums?id={user_id}`

```bash
curl -X GET "http://127.0.0.1:8000/albums?id=1"
```

##### `GET /todos?id={user_id}`

```bash
curl -X GET "http://127.0.0.1:8000/todos?id=1"
```

---
### 🚀 Uso con Postman

Para una experiencia de prueba más robusta e interactiva, se proporciona una **Colección** y un **Entorno** para Postman. Esto te permitirá probar todos los endpoints de forma organizada y con variables reutilizables.

> [!NOTE]
> La **Colección** contiene todas las peticiones de la API preconfiguradas. El **Entorno** almacena variables como la URL base (`baseUrl`) para que no tengas que escribirla repetidamente.

---

#### 1. Preparación de los Archivos

Primero, crea los siguientes dos archivos en tu máquina local. Puedes nombrarlos como quieras, pero se recomienda usar los nombres sugeridos.

*   **`Postman_Collection.json`** (Contiene las peticiones de la API)
    ```json
    {
        "info": { "_postman_id": "c1f2b3c4-d5e6-f7a8-b9c0-d1e2f3a4b5c6", "name": "JSONPlaceholder API Proxy", "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json" },
        "item": [
            { "name": "Get Root", "request": { "method": "GET", "url": { "raw": "{{baseUrl}}/", "host": ["{{baseUrl}}"] } } },
            { "name": "Get Health", "request": { "method": "GET", "url": { "raw": "{{baseUrl}}/health", "host": ["{{baseUrl}}"], "path": ["health"] } } },
            { "name": "Get User by ID", "request": { "method": "GET", "url": { "raw": "{{baseUrl}}/users/{{userId}}", "host": ["{{baseUrl}}"], "path": ["users", "{{userId}}"] } } },
            { "name": "Get User Posts", "request": { "method": "GET", "url": { "raw": "{{baseUrl}}/posts?id={{userId}}", "host": ["{{baseUrl}}"], "path": ["posts"], "query": [{"key": "id", "value": "{{userId}}"}] } } },
            { "name": "Get User Albums", "request": { "method": "GET", "url": { "raw": "{{baseUrl}}/albums?id={{userId}}", "host": ["{{baseUrl}}"], "path": ["albums"], "query": [{"key": "id", "value": "{{userId}}"}] } } },
            { "name": "Get User Todos", "request": { "method": "GET", "url": { "raw": "{{baseUrl}}/todos?id={{userId}}", "host": ["{{baseUrl}}"], "path": ["todos"], "query": [{"key": "id", "value": "{{userId}}"}] } } }
        ]
    }
    ```

*   **`Postman_Environment.json`** (Contiene las variables)
    ```json
    {
        "id": "a1b2c3d4-e5f6-a7b8-c9d0-e1f2a3b4c5d6", "name": "Local Environment",
        "values": [
            { "key": "baseUrl", "value": "http://127.0.0.1:8000", "type": "default", "enabled": true },
            { "key": "userId", "value": "1", "type": "default", "enabled": true }
        ],
        "_postman_variable_scope": "environment"
    }
    ```

---

#### 2. Importar y Configurar en Postman

Sigue estos pasos para poner todo en marcha:

1.  **Importar Archivos:**
    *   Abre la aplicación de Postman.
    *   En el panel izquierdo, haz clic en el botón **`Import`**.
    *   Arrastra y suelta los dos archivos JSON (`Postman_Collection.json` y `Postman_Environment.json`) en la ventana de importación.
    *   Confirma la importación.

2.  **Verificar la Importación:**
    *   En el panel izquierdo, ahora deberías ver una nueva colección llamada **"JSONPlaceholder API Proxy"**.
    *   En la misma barra lateral, en la pestaña **"Environments"**, verás **"Local Environment"**.

3.  **Activar el Entorno:**
> [!IMPORTANT]
> Este paso es esencial para que Postman sepa qué significan las variables como `{{baseUrl}}`.

 En la esquina superior derecha de la ventana de Postman, haz clic en el menú desplegable que dice "No environment" y selecciona **"Local Environment"**.

---

#### 3. Ejecutar y Modificar Peticiones

¡Ya está todo listo para probar!

1.  **Asegúrate de que tu API esté corriendo** en tu terminal (`poetry run uvicorn app.main:app --reload`).
2.  En Postman, abre la colección **"JSONPlaceholder API Proxy"** y haz clic en cualquier petición, por ejemplo, **"Get User Posts"**.
3.  Presiona el botón azul **`Send`**. Deberías ver la respuesta exitosa de la API en la parte inferior.

**¿Cómo cambiar el ID del usuario para las pruebas?**

La variable `{{userId}}` está centralizada en el entorno para que puedas probar con diferentes usuarios fácilmente.

1.  En el panel izquierdo, ve a la pestaña **"Environments"** y haz clic en **"Local Environment"**.
2.  Se abrirá una tabla con las variables. Verás la fila de `userId`.
3.  Cambia el valor en la columna **"CURRENT VALUE"** de `1` al ID que quieras probar (por ejemplo, `2`, `5`, etc.).
4.  **No olvides guardar los cambios** (presiona `Ctrl+S` o `Cmd+S`).
5.  Vuelve a ejecutar cualquier petición. Ahora todas usarán automáticamente el nuevo `userId` que has configurado.

## 🧪 Ejecución de Pruebas

El proyecto cuenta con una suite de pruebas para garantizar la calidad y el correcto funcionamiento del código. Para ejecutar todas las pruebas, utiliza `poetry run`, que ejecuta el comando dentro del entorno virtual del proyecto de forma automática:



```bash
poetry run pytest
```

Una salida exitosa se verá así, confirmando que todas las pruebas pasan correctamente:

```
================================================================= test session starts ==================================================================
platform darwin -- Python 3.13.5, pytest-8.4.1, pluggy-1.6.0
rootdir: /path/to/project
configfile: pyproject.toml
plugins: respx-0.22.0, anyio-4.9.0, asyncio-1.1.0
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 10 items                                                                                                                                     

tests/test_endpoint.py ......                                                                                                                    [ 60%]
tests/test_service.py ....                                                                                                                       [100%]

================================================================== 10 passed in 0.26s ==================================================================
```

## 💡 Decisiones de Diseño

> [!NOTE]
> **Estandarización de Respuestas con `BaseResponse`**
> Se creó una clase Pydantic base (`BaseResponse`) para unificar la estructura de todas las respuestas de la API. Este enfoque garantiza que cada respuesta devuelva un cuerpo de datos consistente y metadatos útiles (como un `timestamp`), proporcionando una experiencia predecible y robusta para los consumidores de la API.

> [!NOTE]
> **Estrategia de Pruebas por Capas**
> Las pruebas se dividieron estratégicamente para evaluar cada capa de la aplicación de forma aislada, facilitando la depuración y garantizando la cobertura:
> *   **Pruebas de Servicio (`tests/test_service.py`):** Utilizan `respx` para simular las respuestas de la API externa. Esto permite probar la lógica de negocio y el manejo de la comunicación de red de forma rápida y fiable, sin dependencias externas.
> *   **Pruebas de API (`tests/test_endpoint.py`):** Emplean el `TestClient` de FastAPI y su sistema de `dependency_overrides` para reemplazar la capa de servicio con un *mock*. De esta forma, se prueba la capa de la API (enrutamiento, validación, serialización) de forma independiente a la lógica de negocio.

> [!NOTE]
> **Manejo de Errores Centralizado con un Decorador**
> Para evitar la repetición de bloques `try...except` y promover un código más limpio (principio DRY), se implementó un decorador (`@handle_api_error`). Este decorador intercepta las excepciones en la capa de la API, las registra (`logging`) y las convierte en respuestas HTTP de error estandarizadas, manteniendo los endpoints enfocados únicamente en su lógica de éxito.