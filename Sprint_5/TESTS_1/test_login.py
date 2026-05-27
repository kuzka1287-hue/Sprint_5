from locators import MainPageLocators, LoginPageLocators, ForgotPasswordPageLocators
from data import BASE_URL

class TestLogin:
    def test_login_from_main_button(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).is_displayed()

    def test_login_from_personal_account_button(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).is_displayed()

    def test_login_from_registration_form(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        # Кликаем именно на ссылку «Войти» на странице регистрации
        driver.find_element(*LoginPageLocators.LOGIN_LINK_ON_REGISTER_PAGE).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).is_displayed()

    def test_login_from_forgot_password_form(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*ForgotPasswordPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).is_displayed() 
