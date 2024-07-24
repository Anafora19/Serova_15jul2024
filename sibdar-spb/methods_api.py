import requests
import traceback
import allure

BASE_URL = "https://www.sibdar-spb.ru" 
CART_URL = f"{BASE_URL}/api/cart"
HEADERS = {
    "Content-Type": "application/json"
}

session = requests.Session()

@allure.step("Добавление товара в корзину")
def add_to_cart(item_id, quantity=1):
    try:
        url = f"{CART_URL}/add"
        payload = {
            "item_id": item_id,
            "quantity": quantity
        }
        response = session.post(url, json=payload, headers=HEADERS)
        response.raise_for_status()

        allure.attach(f"Response Status Code: {response.status_code}", name="Status Code", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name="Response Text", attachment_type=allure.attachment_type.TEXT)

        if response.headers.get("Content-Type") == "application/json":
            return response.json()
        else:
            return {"html_response": response.text}
    except requests.exceptions.HTTPError as http_err:
        allure.attach(str(http_err), name="HTTP Error", attachment_type=allure.attachment_type.TEXT)
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        allure.attach(str(req_err), name="Request Error", attachment_type=allure.attachment_type.TEXT)
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        traceback_str = traceback.format_exc()
        allure.attach(traceback_str, name="Exception", attachment_type=allure.attachment_type.TEXT)
        print(f"Error adding item to cart: {e}")
        print(traceback_str)
    return None

@allure.step("Обновление товара в корзине")
def update_cart(item_id, quantity):
    try:
        url = f"{CART_URL}/update"
        payload = {
            "item_id": item_id,
            "quantity": quantity
        }
        response = session.post(url, json=payload, headers=HEADERS)
        response.raise_for_status()

        allure.attach(f"Response Status Code: {response.status_code}", name="Status Code", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name="Response Text", attachment_type=allure.attachment_type.TEXT)

        if response.headers.get("Content-Type") == "application/json":
            return response.json()
        else:
            return {"html_response": response.text}
    except requests.exceptions.HTTPError as http_err:
        allure.attach(str(http_err), name="HTTP Error", attachment_type=allure.attachment_type.TEXT)
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        allure.attach(str(req_err), name="Request Error", attachment_type=allure.attachment_type.TEXT)
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        traceback_str = traceback.format_exc()
        allure.attach(traceback_str, name="Exception", attachment_type=allure.attachment_type.TEXT)
        print(f"Error updating cart: {e}")
        print(traceback_str)
    return None

@allure.step("Удаление товара из корзины")
def remove_from_cart(item_id):
    try:
        url = f"{CART_URL}/remove"
        payload = {
            "item_id": item_id
        }
        response = session.post(url, json=payload, headers=HEADERS)
        response.raise_for_status()

        allure.attach(f"Response Status Code: {response.status_code}", name="Status Code", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name="Response Text", attachment_type=allure.attachment_type.TEXT)

        if response.headers.get("Content-Type") == "application/json":
            return response.json()
        else:
            return {"html_response": response.text}
    except requests.exceptions.HTTPError as http_err:
        allure.attach(str(http_err), name="HTTP Error", attachment_type=allure.attachment_type.TEXT)
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        allure.attach(str(req_err), name="Request Error", attachment_type=allure.attachment_type.TEXT)
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        traceback_str = traceback.format_exc()
        allure.attach(traceback_str, name="Exception", attachment_type=allure.attachment_type.TEXT)
        print(f"Error removing item from cart: {e}")
        print(traceback_str)
    return None

@allure.step("Получение содержимого корзины")
def get_cart_contents():
    try:
        response = session.get(CART_URL, headers=HEADERS)
        response.raise_for_status()

        allure.attach(f"Response Status Code: {response.status_code}", name="Status Code", attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name="Response Text", attachment_type=allure.attachment_type.TEXT)

        if response.headers.get("Content-Type") == "application/json":
            return response.json()
        else:
            return {"html_response": response.text}
    except requests.exceptions.HTTPError as http_err:
        allure.attach(str(http_err), name="HTTP Error", attachment_type=allure.attachment_type.TEXT)
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        allure.attach(str(req_err), name="Request Error", attachment_type=allure.attachment_type.TEXT)
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        traceback_str = traceback.format_exc()
        allure.attach(traceback_str, name="Exception", attachment_type=allure.attachment_type.TEXT)
        print(f"Error getting cart contents: {e}")
        print(traceback_str)
    return None