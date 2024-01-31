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

    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio:", people_checked)
    assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots radio:", robots_checked)
    assert robots_checked is None

    time.sleep(11)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button_disabled = button.get_attribute("disabled")
    print(button_disabled)
    assert button_disabled == "true"

finally:
    time.sleep(10)
    browser.quit()
