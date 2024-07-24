import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

driver = None

def setup_module(module):
    global driver
    if driver is None:  
        driver = webdriver.Firefox()  
        driver.get("https://www.sibdar-spb.ru")

def teardown_module(module):
    global driver
    if driver:
        driver.quit()

def add_to_cart(item_id):
    try:
        if driver is None:
            raise Exception("WebDriver is not initialized. Call setup_module first.")
        
        add_to_cart_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[@class='btn-default js-order' and @onclick=\"addToCard('{item_id}', this, event);\"]"))
        )
        add_to_cart_button.click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "count_bask_right")))
    except Exception as e:
        print(f"Произошла ошибка при добавлении в корзину: {e}")
        print(traceback.format_exc())

def get_cart_contents():
    try:
        if driver is None:
            raise Exception("WebDriver is not initialized. Call setup_module first.")
        
        cart_link = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "bask_btn_right"))
        )
        cart_link.click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='modal order_modal']//div[@class='order_item' and @data-idpr='204']")))
    except Exception as e:
        print(f"Произошла ошибка при проверке содержимого корзины: {e}")
        print(traceback.format_exc())

def remove_from_cart():
    try:
        if driver is None:
            raise Exception("WebDriver is not initialized. Call setup_module first.")
        
        remove_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='delet_pr_bas' and @onclick='deleteCardItem(this, 204)']"))
        )
        remove_button.click()
        WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "count_bask_right"), "0"))
    except Exception as e:
        print(f"Произошла ошибка при удалении из корзины: {e}")
        print(traceback.format_exc())

def get_cart_contents_api():
    try:
        response = requests.get("https://www.sibdar-spb.ru/api/cart")
        response.raise_for_status()  # Проверим, что статус 200 OK
        return response.json()
    except Exception as e:
        print(f"Произошла ошибка при проверке содержимого корзины через API: {e}")
        print(traceback.format_exc())
        return None