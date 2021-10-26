import pytest

from base import BaseCase
import random

from ui.pages.login_error_page import LoginErrorPage
from ui.pages.main_page import MainPage


class Test(BaseCase):

    @pytest.fixture(scope='function')
    def login(self):
        self.login_page.login()
        return MainPage(self.driver)

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

    def test_create_campaign(self, login, repo_root):
        main_page = login
        campaign_creation_page = main_page.click_create_campaign()
        campaign_name = campaign_creation_page.create_campaign(repo_root)
        assert main_page.find(
            (
                main_page.locators.CAMPAIGN_NAME_TEMPLATE[0],
                main_page.locators.CAMPAIGN_NAME_TEMPLATE[1].format(campaign_name)
            )
        )
