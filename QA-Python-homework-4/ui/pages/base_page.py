from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.basic_locators import BasePageLocators

CLICK_RETRY = 3
BASE_TIMEOUT = 10


class BasePage:
    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                self.find(locator, timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except (StaleElementReferenceException, ElementClickInterceptedException):
                if i == CLICK_RETRY - 1:
                    raise

    def send_keys(self, locator, query):
        elem = self.find(locator)
        elem.clear()
        elem.send_keys(query)
        self.driver.hide_keyboard()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = BASE_TIMEOUT
        return WebDriverWait(self.driver, timeout)
