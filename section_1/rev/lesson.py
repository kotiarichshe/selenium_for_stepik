import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"

try:
    # Инициализация драйвера
    browser = webdriver.Chrome()
    # Переход на страницу с формой
    browser.get(link)
    # Заполнение первой формы
    # Находим элемент ввода имени
    first_name_input = browser.find_element(
        By.CSS_SELECTOR, '.first_block .first_class input.form-control.first')
    # Отправляем имя
    first_name_input.send_keys("Иван")

    last_name_input = browser.find_element(
        By.CSS_SELECTOR, '.first_block .second_class input.form-control.second')
    last_name_input.send_keys("Petrov")

    # Находим элемент ввода email
    email_input = browser.find_element(
        By.CSS_SELECTOR, '.first_block .third_class input.form-control.third')
    # Отправляем email
    email_input.send_keys("ivan@yandex.com")

    # Заполнение второй формы
    # Находим элемент ввода номера телефона
    phone_input = browser.find_element(
        By.CSS_SELECTOR, '.second_block .first_class input.form-control.first')
    # Отправляем номер телефона
    phone_input.send_keys("8(903)162-22-78")

    # Находим элемент ввода адреса
    address_input = browser.find_element(
        By.CSS_SELECTOR, '.second_block .second_class input.form-control.second')
    # Отправляем адрес
    address_input.send_keys("Москва")

    # Отправка формы
    submit_button = browser.find_element(
        By.CSS_SELECTOR, 'button.btn.btn-default')
    submit_button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # Находим элемент,содержащий текст с использованием XPath
    welcome_text_elt = browser.find_element(
        By.XPATH, "//h1[contains(text(), 'Congratulations! You have successfully registered!')]")

    # Выводим текст элемента
    print("Текст элемента:", welcome_text_elt.text)
    # Проверка успешной регистрации
    if welcome_text_elt:
        print("Поздравляем! Вы успешно зарегистрировались!")
    else:
        print("Регистрация не удалась.")


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)

# Закрываем браузер после выполнения всех манипуляций
browser.quit()
