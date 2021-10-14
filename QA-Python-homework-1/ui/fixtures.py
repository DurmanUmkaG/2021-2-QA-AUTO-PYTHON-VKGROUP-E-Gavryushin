import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = webdriver.Chrome(executable_path="/home/durmanumka/Downloads/chromedriver")
    browser.maximize_window()
    browser.get(url)
    yield browser
    browser.close()