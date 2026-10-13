# Pre-entrega - Automation Testing

Pruebas automatizadas para el sitio SauceDemo, realizadas con Python, Selenium y Pytest.

## Pruebas

- `test_login.py`: verifica el inicio de sesión.
- `test_inventory.py`: verifica el catálogo y muestra el nombre y el precio del primer producto.
- `test_cart.py`: agrega un producto al carrito y comprueba que aparezca correctamente.

## Requisitos

- Python 3.10 o superior.
- Google Chrome.
- Conexión a Internet.

## Instalación

Clonar el repositorio y entrar en su carpeta:

```bash
git clone https://github.com/wolframium919/pre-entrega-automation-testing-miguel-conforti.git
cd pre-entrega-automation-testing-miguel-conforti
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Ejecutar las pruebas

```bash
python -m pytest
```

Para generar el reporte HTML:

```bash
python -m pytest --html=reports/reporte.html --self-contained-html
```

El resultado HTML se guarda en `reports/reporte.html`. Pytest registra los resultados en `reports/ejecucion.log`. Si una prueba falla, se guarda una captura en `screenshots/`.

## Datos de prueba

- Sitio: https://www.saucedemo.com/
- Usuario: `standard_user`
- Contraseña: `secret_sauce`
