# 🚀 Guía de Uso con Postman

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