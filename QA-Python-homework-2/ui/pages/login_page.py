import os.path

from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):
    locators = LoginPageLocators
    url = 'https://target.my.com/'

    def login(self, is_generate_email=False, is_generate_password=False):
        with open(os.path.join('files', 'credentials'), 'r') as file:
            user_name, password = file.readlines()
        if is_generate_email:
            user_name = self.create_random_email()
        if is_generate_password:
            password = self.create_random_str()
        self.click(self.locators.LOG_IN_LOCATOR)
        self.send_keys(self.locators.USERNAME_LOCATOR, user_name)
        self.send_keys(self.locators.PASSWORD_LOCATOR, password)
        self.click(self.locators.LOG_IN_BUTTON)
