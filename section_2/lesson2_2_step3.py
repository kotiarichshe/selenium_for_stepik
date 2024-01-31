from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    result = str(int(num1) + int(num2))
    print(result)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(result)

    browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()
