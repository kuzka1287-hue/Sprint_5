# Вспомогательная функция для регистрации пользователя
# generators.py (дополнение)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import RegisterPageLocators, MainPageLocators, LoginPageLocators
from data import BASE_URL

def register_user(driver, name, email, password):
    """Регистрирует нового пользователя через UI и возвращает True/False"""
    driver.get(BASE_URL)
    # Клик по кнопке «Войти в аккаунт» на главной
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
    # Переход на страницу регистрации
    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
    # Заполнение формы
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    # Ждём появления кнопки «Войти» на странице логина (успешная регистрация)
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        return True
    except:
        return False 
