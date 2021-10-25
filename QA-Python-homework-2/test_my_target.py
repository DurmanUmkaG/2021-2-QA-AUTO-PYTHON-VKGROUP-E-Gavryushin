from base import BaseCase
import random

from ui.pages.login_error_page import LoginErrorPage


class Test(BaseCase):

    def test_wrong_password(self):
        self.login_page.login(
            password=''.join([chr(random.randint(97, 122)) for _ in range(7)])
        )
        login_error_page = LoginErrorPage(self.driver)
        assert login_error_page.find(login_error_page.locators.ERROR_MESSAGE_LOCATOR).is_displayed()

    def test_wrong_user_name(self):
        self.login_page.login(
            user_name=''.join([chr(random.randint(97, 122)) for _ in range(7)]) +
                      '@' +
                      ''.join([chr(random.randint(97, 122)) for _ in range(7)]) +
                      '.ru'
        )
        login_error_page = LoginErrorPage(self.driver)
        assert login_error_page.find(login_error_page.locators.ERROR_MESSAGE_LOCATOR).is_displayed()
