# 🔌 Guía de Uso de la API

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