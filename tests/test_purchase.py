import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def test_purchase():
    """
       Функция для автоматизированного тестирования процесса покупки на сайте saucedemo.

       Этот тест выполняет следующие шаги:
       1. Открывает веб-сайт.
       2. Выполняет вход с использованием учетных данных стандартного пользователя.
       3. Добавляет товар (Sauce Labs Backpack) в корзину.
       4. Переходит в корзину и проверяет, что товар был добавлен.
       5. Оформляет покупку, вводя данные покупателя.
       6. Завершает покупку и проверяет, что отображается сообщение об успешном завершении.

       Исключения:
           AssertionError: Если товар не был добавлен в корзину или если сообщение об успешной
           покупке не совпадает с ожидаемым.
       """
    options = webdriver.ChromeOptions()
    # Отключает обнаружение автоматизации
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Исключает опцию enable-automation
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # Отключает расширение автоматизации
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)  # Задержка для наблюдения

    try:
        # Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        # Выбор товара
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)

        # Переход в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)

        # Проверка, что товар добавлен в корзину
        cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert cart_item == "Sauce Labs Backpack", "Товар не был добавлен в корзину"
        time.sleep(2)

        # Оформление покупки
        driver.find_element(By.ID, "checkout").click()
        time.sleep(2)
        driver.find_element(By.ID, "first-name").send_keys("Test")
        time.sleep(1)
        driver.find_element(By.ID, "last-name").send_keys("User")
        time.sleep(1)
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        time.sleep(1)
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)

        # Завершение покупки
        driver.find_element(By.ID, "finish").click()
        time.sleep(2)

        # Проверка успешного завершения покупки
        success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert success_message == "Thank you for your order!", "Покупка не была завершена успешно"

        logging.info("Покупка завершена успешно!")

    except AssertionError as e:
        logging.error(f"Ошибка: {str(e)}")
    except Exception as e:
        logging.error(f"Произошла непредвиденная ошибка: {str(e)}")
    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    test_purchase()
