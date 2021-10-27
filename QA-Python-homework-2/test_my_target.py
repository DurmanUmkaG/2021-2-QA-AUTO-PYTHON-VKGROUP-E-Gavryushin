import pytest

from base import BaseCase

from ui.pages.login_error_page import LoginErrorPage
from ui.pages.main_page import MainPage


class Test(BaseCase):

    @pytest.fixture(scope='function')
    def login(self):
        self.login_page.login()
        return MainPage(self.driver)

    @pytest.mark.UI
    def test_wrong_password(self):
        self.login_page.login(
            password=self.base_page.create_random_str()
        )
        login_error_page = LoginErrorPage(self.driver)
        assert login_error_page.find(login_error_page.locators.ERROR_MESSAGE_LOCATOR).is_displayed()

    @pytest.mark.UI
    def test_wrong_user_name(self):
        self.login_page.login(
            user_name=self.base_page.create_random_str() +
                      '@' +
                      self.base_page.create_random_str() +
                      '.ru'
        )
        login_error_page = LoginErrorPage(self.driver)
        assert login_error_page.find(login_error_page.locators.ERROR_MESSAGE_LOCATOR).is_displayed()

    @pytest.mark.UI
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

    @pytest.mark.UI
    def test_create_segment(self, login):
        main_page = login
        audiences_page = main_page.go_to_audiences_page()
        segment_name = audiences_page.create_segment()
        assert audiences_page.find((
            audiences_page.locators.SEGMENT_IN_LIST_TEMPLATE[0],
            audiences_page.locators.SEGMENT_IN_LIST_TEMPLATE[1].format(segment_name)
        )).is_displayed()

    @pytest.mark.UI
    def test_delete_segment(self, login):
        main_page = login
        audiences_page = main_page.go_to_audiences_page()
        assert audiences_page.is_segment_deleted()
