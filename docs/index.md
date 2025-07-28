# API Proxy para JSONPlaceholder

_Un servicio backend robusto construido con FastAPI y Python como parte de una prueba técnica._

[![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1+-darkgreen?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Poetry](https://img.shields.io/badge/Poetry-1.8.2-blueviolet?logo=poetry)](https://python-poetry.org/)
[![Pytest](https://img.shields.io/badge/Pytest-8.4.1+-blue?logo=pytest)](https://pytest.org/)

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