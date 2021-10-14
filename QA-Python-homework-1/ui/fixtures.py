import pytest
from selenium import webdriver
from ui.pages.base_page import BasePage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = webdriver.Chrome(executable_path="/home/durmanumka/Downloads/chromedriver")
    browser.maximize_window()
    browser.get(url)
    yield browser
    browser.close()
