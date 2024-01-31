from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


link = "http://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    input_firstname = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input_firstname.send_keys("Vladimir")
    input_lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input_lastname.send_keys("Smirnov")
    input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input_email.send_keys("Smirnov@mail.ru")
    input_file = browser.find_element(By.CSS_SELECTOR, '[name="file"]')
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'file.txt')
    input_file.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
