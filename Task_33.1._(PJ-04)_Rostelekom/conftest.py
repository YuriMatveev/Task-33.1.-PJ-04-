import pytest
from selenium import webdriver

from pages.auth_page import AuthPage
from settings import PATH


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(executable_path=PATH)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def auth(browser):
    auth = AuthPage(browser)
    return auth
