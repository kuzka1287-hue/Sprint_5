import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, ForgotPasswordPageLocators
from generators import generate_unique_email, generate_valid_password, register_user
from data import BASE_URL

class TestLogin:
    @pytest.fixture(autouse=True)
    def create_user(self, driver):
        """Фикстура создаёт пользователя для всех тестов входа"""
        self.email = generate_unique_email()
        self.password = generate_valid_password()
        self.name = "Николай"
        register_user(driver, self.name, self.email, self.password)
        driver.get(BASE_URL)  # возвращаемся на главную после регистрации

    def login(self, driver):
        """Общая логика входа (заполнение полей и клик)"""
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(self.email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(self.password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    # 1. Вход через кнопку «Войти в аккаунт» на главной
    def test_login_from_main_button(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
        self.login(driver)
        # После входа должна открыться главная страница (виден конструктор)
        assert driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).is_displayed()

    # 2. Вход через кнопку «Личный кабинет»
    def test_login_from_personal_account_button(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        self.login(driver)
        assert driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).is_displayed()

    # 3. Вход через кнопку в форме регистрации
    def test_login_from_registration_form(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        # На форме регистрации есть ссылка «Войти» (кнопка входа)
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()  # переходим на логин
        self.login(driver)
        assert driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).is_displayed()

    # 4. Вход через кнопку в форме восстановления пароля
    def test_login_from_forgot_password_form(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*ForgotPasswordPageLocators.LOGIN_BUTTON).click()
        self.login(driver)
        assert driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).is_displayed() 
