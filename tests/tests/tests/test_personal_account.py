import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, PersonalAccountLocators
from generators import generate_unique_email, generate_valid_password, register_user
from data import BASE_URL

class TestPersonalAccount:
    @pytest.fixture(autouse=True)
    def login_user(self, driver):
        """Создаём и логиним пользователя перед тестами"""
        email = generate_unique_email()
        password = generate_valid_password()
        name = "Николай"
        register_user(driver, name, email, password)
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_BUTTON))

    # Переход в личный кабинет по клику на «Личный кабинет»
    def test_go_to_personal_account(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccountLocators.ORDER_HISTORY))
        assert driver.find_element(*PersonalAccountLocators.ORDER_HISTORY).is_displayed()

    # Переход из личного кабинета в конструктор по клику на «Конструктор»
    def test_go_to_constructor_from_personal_account(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccountLocators.ORDER_HISTORY))
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        assert driver.find_element(*MainPageLocators.BUNS_TAB).is_displayed()

    # Переход из личного кабинета на главную по клику на логотип Stellar Burgers
    def test_go_to_main_from_logo(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccountLocators.ORDER_HISTORY))
        driver.find_element(*MainPageLocators.LOGO).click()
        assert driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).is_displayed()

    # Выход из аккаунта по кнопке «Выйти» в личном кабинете
    def test_logout(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))
        driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()
        # После выхода появляется кнопка «Войти»
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON_MAIN))
        assert driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).is_displayed() 
