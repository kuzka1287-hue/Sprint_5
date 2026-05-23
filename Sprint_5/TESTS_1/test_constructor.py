import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, ConstructorLocators
from data import BASE_URL

class TestConstructor:
    def test_switch_to_buns_tab(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.SAUCES_TAB).click()  # переключаем на Соусы
        driver.find_element(*MainPageLocators.BUNS_TAB).click()
        # Активный таб – Булки
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
  
