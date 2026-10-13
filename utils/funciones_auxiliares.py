from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"
USUARIO = "standard_user"
CONTRASENA = "secret_sauce"


def iniciar_sesion(driver):
    driver.get(URL)
    espera = WebDriverWait(driver, 10)

    espera.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys(USUARIO)

    driver.find_element(By.ID, "password").send_keys(CONTRASENA)
    driver.find_element(By.ID, "login-button").click()

    espera.until(EC.url_contains("inventory.html"))
    return espera
