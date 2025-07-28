# 🐳 Dockerización

Docker es la forma recomendada para ejecutar la aplicación en un entorno de producción, ya que encapsula la aplicación con todas sus dependencias y configuraciones en una imagen de contenedor aislada y portátil.

### Construir la imagen localmente

Si deseas construir la imagen de Docker desde cero en tu máquina local, puedes usar el siguiente comando. Asegúrate de estar en el directorio raíz del proyecto donde se encuentra el `Dockerfile`.

```bash
docker build -t jemeza06/jsonplaceholder-proxy:latest .
```

### Ejecutar desde Docker Hub (Recomendado)

La forma más fácil y rápida de poner en marcha la aplicación es ejecutar la imagen preconstruida directamente desde Docker Hub.

1.  **Ejecuta el siguiente comando:**
    Este comando descargará la imagen `jemeza06/jsonplaceholder-proxy:latest`, iniciará un contenedor en segundo plano (`-d`), mapeará el puerto 8000 del contenedor al puerto 8000 de tu máquina (`-p 8000:8000`) y le asignará un nombre fácil de recordar (`--name jsonplaceholder-proxy-container`).

    ```bash
    docker run -d -p 8000:8000 --name jsonplaceholder-proxy-container jemeza06/jsonplaceholder-proxy:latest
    ```

2.  **¡Listo!**
    Una vez que el contenedor esté corriendo, la API estará disponible y podrás acceder a la documentación interactiva en `http://localhost:8000/docs`.