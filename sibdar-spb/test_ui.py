import methods_ui
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='module', autouse=True)
def driver_setup_teardown():
    methods_ui.setup_module(None)
    yield
    methods_ui.teardown_module(None)

@allure.feature('Cart Operations')
def test_add_to_cart():
    methods_ui.add_to_cart(item_id=204)

    # Проверить, что товар добавлен в корзину
    cart_count = methods_ui.driver.find_element(By.CLASS_NAME, "count_bask_right")
    WebDriverWait(methods_ui.driver, 30).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "count_bask_right"), "1"))
    assert "1" in cart_count.text
    print("Товар успешно добавлен в корзину.")

@allure.feature('Cart Operations')
def test_cart_contains_item():
    methods_ui.get_cart_contents()

    # Проверить, что в корзине есть товар с id 204
    cart_item = WebDriverWait(methods_ui.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='modal order_modal']//div[@class='order_item' and @data-idpr='204']"))
    )
    assert cart_item is not None
    print("Товар с id 204 найден в корзине.")

@allure.feature('Cart Operations')
def test_remove_from_cart():
    methods_ui.remove_from_cart()

    # Проверить, что корзина пуста
    cart_count = methods_ui.driver.find_element(By.CLASS_NAME, "count_bask_right")
    WebDriverWait(methods_ui.driver, 30).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "count_bask_right"), "0"))
    assert "0" in cart_count.text
    print("Товар успешно удален из корзины.")

    # Проверить, что отображается сообщение о пустой корзине
    empty_cart_message = WebDriverWait(methods_ui.driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='body_order' and @id='order-list']/h2"))
    )
    assert "Корзина пуста, необходимо это исправить" in empty_cart_message.text
    print("Корзина пуста, сообщение отображается.")


if __name__ == "__main__":
    with pytest.raises(SystemExit):
        pytest.main([__file__])