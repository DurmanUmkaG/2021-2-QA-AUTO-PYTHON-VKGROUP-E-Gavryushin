from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):
    locators = LoginPageLocators

    def login(self, user_name='gavryushin2000@internet.ru', password='A^_iZ^cbF6BAb*F'):
        self.click(self.locators.LOG_IN_LOCATOR)
        self.send_keys(self.locators.USERNAME_LOCATOR, user_name)
        self.send_keys(self.locators.PASSWORD_LOCATOR, password, Keys.RETURN)
