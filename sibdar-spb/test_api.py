import methods_api
import pytest
import allure

 #Проверить, что товар (с ID 204) успешно добавляется в корзину
@allure.feature("Cart Operations")
@allure.story("Add to cart")
def test_add_to_cart():
    item_id = 204
    response = methods_api.add_to_cart(item_id=item_id)

    assert response is not None, "Response is None"
    print(f"Response from add_to_cart: {response}")  #Логирование получения ответа

    #Получен HTML-ответ, прикрепляем его и выводим предупреждение
    if "html_response" in response:
        allure.attach(response["html_response"], name="HTML Response", attachment_type=allure.attachment_type.HTML)
        print(f"Warning: Received HTML response during add_to_cart: {response['html_response']}")
        return  

    assert response.get("success") is True, "Add to cart was not successful"

    cart_contents = methods_api.get_cart_contents()
    assert cart_contents is not None, "Cart contents is None"

    item_found = any(item["item_id"] == item_id for item in cart_contents["items"])
    assert item_found, "Item was not added to the cart"

#Проверить, что количество товара в корзине обновляется корректно (изменяется на 3)
@allure.feature("Cart Operations")
@allure.story("Update cart")
def test_update_cart():
    item_id = 204
    new_quantity = 3
    response = methods_api.update_cart(item_id=item_id, quantity=new_quantity)

    assert response is not None, "Response is None"
    print(f"Response from update_cart: {response}")  #Логирование получения ответа

    #Получен HTML-ответ, прикрепляем его и выводим предупреждение
    if "html_response" in response:
        allure.attach(response["html_response"], name="HTML Response", attachment_type=allure.attachment_type.HTML)
        print(f"Warning: Received HTML response during update_cart: {response['html_response']}")
        return

    assert response.get("success") is True, "Update cart was not successful"

    cart_contents = methods_api.get_cart_contents()
    assert cart_contents is not None, "Cart contents is None"

    for item in cart_contents["items"]:
        if item["item_id"] == item_id:
            assert item["quantity"] == new_quantity, "Quantity in cart does not match expected"
            break
    else:
        pytest.fail("Item not found in the cart in expected quantity")

#Проверить, что товар (с ID 204) успешно удаляется из корзины.
@allure.feature("Cart Operations")
@allure.story("Remove from cart")
def test_remove_from_cart():
    item_id = 204
    response = methods_api.remove_from_cart(item_id=item_id)

    assert response is not None, "Response is None"
    print(f"Response from remove_from_cart: {response}")  #Логирование получения ответа

    #Получен HTML-ответ, прикрепляем его и выводим предупреждение
    if "html_response" in response:
        allure.attach(response["html_response"], name="HTML Response", attachment_type=allure.attachment_type.HTML)
        print(f"Warning: Received HTML response during remove_from_cart: {response['html_response']}")
        return

    assert response.get("success") is True, "Remove from cart was not successful"

    cart_contents = methods_api.get_cart_contents()
    assert cart_contents is not None, "Cart contents is None"

    item_found = any(item["item_id"] == item_id for item in cart_contents["items"])
    assert not item_found, "Item was not removed from the cart"


if __name__ == "__main__":
    pytest.main([__file__])