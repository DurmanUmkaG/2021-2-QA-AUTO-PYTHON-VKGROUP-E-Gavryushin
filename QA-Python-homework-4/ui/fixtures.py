import pytest
from appium import webdriver

from ui.capability import capability_select


@pytest.fixture(scope='function')
def driver(config, apk_path):
    appium_url = config['appium']
    driver = webdriver.Remote(appium_url, desired_capabilities=capability_select(apk_path))
    yield driver
    driver.quit()
