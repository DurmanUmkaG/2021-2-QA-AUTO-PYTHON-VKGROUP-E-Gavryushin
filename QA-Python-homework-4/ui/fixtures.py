import pytest
from appium import webdriver

from ui.capability import capability_select
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture(scope='function')
def driver(config, apk_path):
    appium_url = config['appium']
    driver = webdriver.Remote(appium_url, desired_capabilities=capability_select(apk_path))
    yield driver
    driver.quit()
