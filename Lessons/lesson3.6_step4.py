from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.get("https://stepik.org/lesson/236895/step/1")
    time.sleep(3)
    input1 = browser.find_element(By.ID, "ember33")
    input1.click()
    input2 = browser.find_element(By.ID, "id_login_email")
    input2.send_keys("atticus@inbox.ru")
    input3 = browser.find_element(By.ID, "id_login_password")
    input3.send_keys("Blink182")
    button = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()