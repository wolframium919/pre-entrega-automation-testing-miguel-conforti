import logging
import os
import pytest
from selenium import webdriver

os.makedirs("reports", exist_ok=True)
os.makedirs("screenshots", exist_ok=True)

logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    yield navegador
    navegador.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()

    if reporte.when == "call":
        if reporte.passed:
            logger.info("PASSED: %s", item.name)
        elif reporte.failed:
            logger.error("FAILED: %s", item.name)
            navegador = item.funcargs.get("driver")
            if navegador:
                nombre = item.name + ".png"
                ruta = os.path.join("screenshots", nombre)
                navegador.save_screenshot(ruta)
                logger.info("Captura guardada en: %s", ruta)
        elif reporte.skipped:
            logger.warning("SKIPPED: %s", item.name)
