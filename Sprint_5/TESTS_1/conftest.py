import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, LoginPageLocators
from generators import generate_unique_email, generate_valid_password, register_user
from data import BASE_URL, TEST_USER_NAME

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
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

@pytest.fixture(scope="function")
def registered_user(driver):
    """Фикстура создаёт одного тестового пользователя и возвращает его данные"""
    email = generate_unique_email()
    password = generate_valid_password()
    register_user(driver, TEST_USER_NAME, email, password)
    return {"email": email, "password": password, "name": TEST_USER_NAME}

@pytest.fixture(scope="function")
def logged_in_user(driver, registered_user):
    """Фикстура логинит созданного пользователя на главной странице"""
    driver.get(BASE_URL)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_BUTTON))
    return registered_user 
