from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, \
    TimeoutException
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

    @property
    def touch_action(self):
        return TouchAction(self.driver)

    def swipe_element_to_left(self, locator):
        web_element = self.find(locator, 10)
        left_x = web_element.location['x']
        right_x = left_x + web_element.rect['width']
        upper_y = web_element.location['y']
        lower_y = upper_y + web_element.rect['height']
        middle_y = (upper_y + lower_y) / 2
        self.touch_action. \
            press(x=right_x, y=middle_y). \
            wait(ms=300). \
            move_to(x=left_x, y=middle_y). \
            release(). \
            perform()

    def swipe_to_element(self, swiped_locator, locator, max_swipes):
        already_swiped = 0
        while len(self.driver.find_elements(*locator)) == 0:
            if already_swiped > max_swipes:
                raise TimeoutException(f'Error with {locator}, please check function')
            self.swipe_element_to_left(swiped_locator)
            already_swiped += 1

    def wait(self, timeout=None):
        if timeout is None:
            timeout = BASE_TIMEOUT
        return WebDriverWait(self.driver, timeout)
