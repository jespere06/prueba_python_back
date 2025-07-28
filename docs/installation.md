# ⚙️ Instalación y Ejecución

## Requisitos Previos

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
    & "$VENV_PATH\Scriptsctivate.ps1"
    ```

5.  **Iniciar el servidor de desarrollo:**
    Una vez activado el entorno, usa `uvicorn` para iniciar la aplicación. El flag `--reload` reiniciará el servidor automáticamente tras cada cambio en el código.
    ```bash
    uvicorn app.main:app --reload
    ```

6.  **¡Listo!**
    La API estará disponible en `http://127.0.0.1:8000`.