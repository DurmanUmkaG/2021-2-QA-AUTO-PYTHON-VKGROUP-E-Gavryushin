import pytest
from selenium import webdriver
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = webdriver.Chrome(executable_path="/home/durmanumka/Downloads/chromedriver")
    browser.maximize_window()
    browser.get(url)
    yield browser
    browser.close()
