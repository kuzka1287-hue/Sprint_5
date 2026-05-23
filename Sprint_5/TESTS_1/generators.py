import random
import string
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators
from data import BASE_URL

FIRST_NAME = "nikolay"
LAST_NAME = "kuznetsov"
COHORT = "46"
DOMAIN = "@yandex.ru"

def generate_unique_email():
    random_digits = ''.join(random.choices(string.digits, k=3))
    email = f"{FIRST_NAME}_{LAST_NAME}_{COHORT}_{random_digits}{DOMAIN}"
    return email.lower()

def generate_valid_password():
    length = random.randint(6, 10)
    letters = string.ascii_letters + string.digits
    return ''.join(random.choices(letters, k=length))

def generate_invalid_password():
    length = random.randint(1, 5)
    letters = string.ascii_letters + string.digits
    return ''.join(random.choices(letters, k=length))

def register_user(driver, name, email, password):
    """Регистрирует пользователя через UI. Возвращает True при успехе, иначе False."""
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    # Ждём появления кнопки «Войти» на странице входа
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        return True
    except:
        return False