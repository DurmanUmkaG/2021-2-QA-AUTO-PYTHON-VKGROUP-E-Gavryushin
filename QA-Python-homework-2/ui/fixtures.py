import logging

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    manager = ChromeDriverManager(version='latest', log_level=logging.CRITICAL)
    browser = webdriver.Chrome(executable_path=manager.install())
    browser.maximize_window()
    browser.get(url)
    yield browser
    browser.quit()