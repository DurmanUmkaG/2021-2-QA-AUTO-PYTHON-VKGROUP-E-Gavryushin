import logging

import allure

from ui.locators.basic_locators import BasePageLocators
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
import random

CLICK_RETRY = 3
BASE_TIMEOUT = 10


class BasePage:
    locators = BasePageLocators
    url = 'https://target.my.com/'

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('test')
        self.is_opened()

    def create_random_email(self):
        return (self.create_random_str() +
                '@' +
                self.create_random_str() +
                '.ru')

    @staticmethod
    def create_random_str():
        return ''.join([chr(random.randint(97, 122)) for _ in range(7)])

    def wait(self, timeout=None):
        if timeout is None:
            timeout = BASE_TIMEOUT
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def send_keys(self, locator, query):
        search = self.find(locator)
        search.clear()
        search.send_keys(query)

    @allure.step('Clicking on {locator}')
    def click(self, locator, timeout=None):
        self.logger.info(f'Clicking on {locator}')
        for i in range(CLICK_RETRY):
            try:
                self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except (StaleElementReferenceException, ElementClickInterceptedException):
                if i == CLICK_RETRY - 1:
                    raise

    def is_opened(self, timeout=None):
        self.wait(timeout).until(EC.url_contains(self.url))
        if len(self.driver.find_elements(*BasePageLocators.SPINNER_LOCATOR)) > 0:
            self.wait(timeout).until(EC.invisibility_of_element_located(BasePageLocators.SPINNER_LOCATOR))
