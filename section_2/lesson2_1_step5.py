from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin((int(x))))))


link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input_text = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_text.send_keys(y)
    input_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input_checkbox.click()
    input_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    input_radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
