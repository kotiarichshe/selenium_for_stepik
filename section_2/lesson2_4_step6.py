from selenium import webdriver
from selenium.webdriver.common.by import By

brouwser = webdriver.Chrome()
brouwser.implicitly_wait(5)

brouwser.get('http://suninjuly.github.io/cats.html')

button = brouwser.find_element(By.ID, "button")
button.click()

