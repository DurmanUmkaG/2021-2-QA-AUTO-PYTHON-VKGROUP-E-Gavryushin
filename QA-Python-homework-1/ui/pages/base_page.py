from ui.locators.basic_locators import BasePageLocators
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException

CLICK_RETRY = 3


class BasePage:
    locators = BasePageLocators

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def send_keys(self, locator, *query):
        search = self.find(locator)
        search.clear()
        for q in query:
            search.send_keys(q)

    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                self.wait(timeout).until(EC.invisibility_of_element_located(BasePageLocators.SPINNER_LOCATOR))
                elem = self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except (StaleElementReferenceException, ElementClickInterceptedException):
                if i == CLICK_RETRY - 1:
                    raise
