from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input2.send_keys(y)
    button1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    button1.click()
    button2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    button2.click()
    button3 = browser.find_element(By.XPATH, "//*[text()='Submit']")
    button3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
