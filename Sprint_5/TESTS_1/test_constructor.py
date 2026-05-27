from locators import MainPageLocators
from data import BASE_URL

class TestConstructor:
    def test_switch_to_buns_tab(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.SAUCES_TAB).click()
        driver.find_element(*MainPageLocators.BUNS_TAB).click()
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        assert active_tab == "Булки"

    def test_switch_to_sauces_tab(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.SAUCES_TAB).click()
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        assert active_tab == "Соусы"

    def test_switch_to_fillings_tab(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.FILLINGS_TAB).click()
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        assert active_tab == "Начинки"
 
