# 🧪 Ejecución de Pruebas

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