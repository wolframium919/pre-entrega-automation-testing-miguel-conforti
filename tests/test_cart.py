from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.funciones_auxiliares import iniciar_sesion


def test_agregar_primer_producto_al_carrito(driver):
    espera = iniciar_sesion(driver)

    producto = espera.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    nombre_esperado = producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text
    precio_esperado = producto.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    boton = producto.find_element(By.CSS_SELECTOR, "button.btn_inventory")
    boton.click()

    contador = espera.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert contador.text == "1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    espera.until(EC.url_contains("cart.html"))

    producto_carrito = espera.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    nombre_carrito = producto_carrito.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text
    precio_carrito = producto_carrito.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    assert nombre_carrito == nombre_esperado
    assert precio_carrito == precio_esperado
