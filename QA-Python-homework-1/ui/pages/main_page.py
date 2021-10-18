import random

from ui.pages.base_page import BasePage
from ui.locators.main_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    locators = MainPageLocators

    def logout(self):
        self.click(self.locators.BALANCE_LOCATOR)
        self.click(self.locators.LOG_OF_LOCATOR)

    def change_contact_information(self):
        full_name = ''.join([chr(random.randint(97, 122)) for _ in range(7)])
        contact_phone_number = ''.join(["7"] + [str(random.randint(0, 9)) for _ in range(10)])
        self.click(self.locators.PROFILE_LOCATOR)
        self.send_keys(self.locators.FULLNAME_LOCATOR, full_name)
        self.send_keys(self.locators.PHONE_NUMBER_LOCATOR, contact_phone_number)
        self.click(self.locators.SAVE_BUTTON_LOCATOR)
        self.find(self.locators.SAVE_NOTIFICATION_LOCATOR)
        self.wait().until(EC.visibility_of_element_located(self.locators.SAVE_NOTIFICATION_LOCATOR))
        return full_name, contact_phone_number
