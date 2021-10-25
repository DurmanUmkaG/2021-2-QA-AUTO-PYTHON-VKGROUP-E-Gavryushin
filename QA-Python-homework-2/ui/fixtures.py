import logging

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    manager = ChromeDriverManager(version='latest', log_level=logging.CRITICAL)
    browser = webdriver.Chrome(executable_path=manager.install())
    browser.maximize_window()
    browser.get(url)
    yield browser
    browser.quit()
