import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Vladimir")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        input2.send_keys("Sherbakov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input3.send_keys("abcd@dcba.ab")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        input1.send_keys("Vladimir")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        input2.send_keys("Sherbakov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        input3.send_keys("abcd@dcba.ab")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()