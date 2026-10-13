from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.funciones_auxiliares import iniciar_sesion


def test_login_exitoso(driver):
    espera = iniciar_sesion(driver)

    assert "inventory.html" in driver.current_url

    titulo = espera.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert titulo.text == "Products"

    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.text == "Swag Labs"
