from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin((int(x))))))

link = "http://suninjuly.github.io/execute_script.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    print(x, y)

    input_text = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_text.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    input_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input_checkbox.click()
    input_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    input_radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
