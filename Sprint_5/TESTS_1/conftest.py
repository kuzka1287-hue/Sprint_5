from typing import Dict, Any
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators
from generators import generate_unique_email, generate_valid_password
from data import BASE_URL, TEST_USER_NAME

def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")

@pytest.fixture(scope="function")
def driver(request: pytest.FixtureRequest) -> WebDriver:
    browser: str = request.config.getoption("--browser")
    if browser == "chrome":
        options = Options()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError("Unsupported browser")
    yield driver
    driver.quit()

def register_user(driver: WebDriver, name: str, email: str, password: str) -> bool:
    """Регистрирует нового пользователя через UI. Возвращает True при успехе."""
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    # Ожидаем появления кнопки «Войти» на странице логина
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
    return True

@pytest.fixture(scope="function")
def registered_user(driver: WebDriver) -> Dict[str, str]:
    email = generate_unique_email()
    password = generate_valid_password()
    register_user(driver, TEST_USER_NAME, email, password)
    return {"email": email, "password": password, "name": TEST_USER_NAME}

@pytest.fixture(scope="function")
def logged_in_user(driver: WebDriver, registered_user: Dict[str, str]) -> Dict[str, str]:
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_BUTTON))
    return registered_user
