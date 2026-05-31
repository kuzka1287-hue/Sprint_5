from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, PersonalAccountLocators

class TestPersonalAccount:
    def test_go_to_personal_account(self, driver, logged_in_user):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccountLocators.ORDER_HISTORY))
        assert driver.find_element(*PersonalAccountLocators.ORDER_HISTORY).is_displayed()

    def test_go_to_constructor_from_personal_account(self, driver, logged_in_user):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccountLocators.ORDER_HISTORY))
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        assert driver.find_element(*MainPageLocators.BUNS_TAB).is_displayed()

    def test_go_to_main_from_logo(self, driver, logged_in_user):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccountLocators.ORDER_HISTORY))
        driver.find_element(*MainPageLocators.LOGO).click()
        assert driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).is_displayed()

    def test_logout(self, driver, logged_in_user):
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))
        driver.find_element(*PersonalAccountLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON_MAIN))
        assert driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).is_displayed()  
