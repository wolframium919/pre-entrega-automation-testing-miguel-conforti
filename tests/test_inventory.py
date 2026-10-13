from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.funciones_auxiliares import iniciar_sesion


def test_catalogo_muestra_productos_y_controles(driver):
    espera = iniciar_sesion(driver)

    titulo = espera.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert titulo.text == "Products"

    productos = espera.until(
        EC.visibility_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )
    assert len(productos) > 0

    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert menu.is_displayed()
    assert filtro.is_displayed()

    nombre = productos[0].find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text
    precio = productos[0].find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    print("Primer producto:", nombre)
    print("Precio:", precio)
    assert nombre != ""
    assert precio.startswith("$")
