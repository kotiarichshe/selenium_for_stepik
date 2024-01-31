from selenium import webdriver
from selenium.webdriver.common.by import By

brouwser = webdriver.Chrome()
brouwser.implicitly_wait(5)

brouwser.get('http://suninjuly.github.io/wait1.html')

button = brouwser.find_element(By.ID, "verify")
button.click()
message = brouwser.find_element(By.ID, "verify_message")

assert "successful" in message.text
