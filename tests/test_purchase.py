import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def test_purchase():
    # Настройка драйвера
    driver = webdriver.Chrome()  # Убедитесь, что у вас установлен ChromeDriver
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)  # Задержка для наблюдения

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(1)  # Задержка для наблюдения
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(1)  # Задержка для наблюдения
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)  # Задержка для наблюдения

    # Выбор товара
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)  # Задержка для наблюдения

    # Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)  # Задержка для наблюдения

    # Проверка, что товар добавлен в корзину
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert cart_item == "Sauce Labs Backpack", "Товар не был добавлен в корзину"
    time.sleep(2)  # Задержка для наблюдения

    # Оформление покупки
    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)  # Задержка для наблюдения
    driver.find_element(By.ID, "first-name").send_keys("Test")
    time.sleep(1)  # Задержка для наблюдения
    driver.find_element(By.ID, "last-name").send_keys("User")
    time.sleep(1)  # Задержка для наблюдения
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    time.sleep(1)  # Задержка для наблюдения
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)  # Задержка для наблюдения

    # Завершение покупки
    driver.find_element(By.ID, "finish").click()
    time.sleep(2)  # Задержка для наблюдения

    # Проверка успешного завершения покупки
    success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert success_message == "Thank you for your order!", "Покупка не была завершена успешно"

    # Логирование успешного завершения покупки
    logging.info("Покупка завершена успешно!")

    time.sleep(2)  # Задержка для наблюдения

    # Закрытие браузера
    driver.quit()


if __name__ == "__main__":
    test_purchase()
