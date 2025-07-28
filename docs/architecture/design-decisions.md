# 💡 Decisiones de Diseño

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