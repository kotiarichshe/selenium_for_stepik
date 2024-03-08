import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope="function")
def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
        return config


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function", autouse=True)
def test_authorization(browser, load_config):
    login = load_config["login_stepik"]
    password = load_config["password_stepik"]
    link = "https://stepik.org/lesson/236895/step/1"
    browser.implicitly_wait(30)
    browser.get(link)
    button_auth = browser.find_element(By.CSS_SELECTOR, "a.navbar__auth_login")
    button_auth.click()
    input_login = browser.find_element(By.CSS_SELECTOR, '[name="login"]')
    input_login.send_keys(login)
    input_password = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
    input_password.send_keys(password)
    button_loader = browser.find_element(By.CSS_SELECTOR, ".button_with-loader")
    button_loader.click()
    time.sleep(5)


links = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]



class TestMainPage:
    @pytest.mark.parametrize('link', links)
    def test_page_stepik(self, browser, link):
        browser.get(link)
        # if browser.find_element(By.CSS_SELECTOR, ".again-btn.white"):
        #     browser.find_element(By.CSS_SELECTOR, ".again-btn.white").click()
        #     browser.find_element(By.CSS_SELECTOR, '.modal-popup__footer.ember-view button:first-child').click()
        input_answer = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")
        time.sleep(2)
        answer = math.log(int(time.time()))
        input_answer.send_keys(answer)
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
        time.sleep(50)



