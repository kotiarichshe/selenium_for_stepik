from selenium import webdriver
from selenium.webdriver.common.by import By
import time

brouwser = webdriver.Chrome()
brouwser.get('http://suninjuly.github.io/wait1.html')

time.sleep(1)
button = brouwser.find_element(By.ID, "verify")
button.click()
message = brouwser.find_element(By.ID, "verify_message")

assert "successful" in message.text
