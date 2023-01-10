from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".form-group :last-child")
    input3.send_keys("sfsfdf@fsf.hfh")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
