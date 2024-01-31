from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

brouser = webdriver.Chrome()

brouser.get("http://suninjuly.github.io/wait2.html")

button = WebDriverWait(brouser, 5).until(
    EC.element_to_be_clickable((By.ID, "verify"))
)
button.click()
message = brouser.find_element(By.ID, "verify_message")

assert "successful" in message.text
