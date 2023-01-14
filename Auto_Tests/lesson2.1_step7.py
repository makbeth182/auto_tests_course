from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "treasure")
    treasureX = x_element.get_attribute("valuex")
    y = calc(treasureX)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
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

