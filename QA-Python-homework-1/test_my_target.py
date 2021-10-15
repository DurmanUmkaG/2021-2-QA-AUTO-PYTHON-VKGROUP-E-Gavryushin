import pytest
from base import BaseCase
from ui.locators.main_locators import MainPageLocators


class Test(BaseCase):
    @pytest.fixture(scope='function')
    def login(self):
        self.login_page.login()

    def test_login(self, login):
        assert self.driver.current_url == 'https://target.my.com/dashboard'

    def test_logout(self, login):
        self.main_page.logout()
        assert self.driver.current_url == 'https://target.my.com/'

    def test_change_contact_information(self, login):
        full_name, contact_phone_number = self.main_page.change_contact_information()
        changed_full_name = self.main_page.find(self.main_page.locators.FULLNAME_LOCATOR).get_attribute('value')
        changed_contact_phone_number = self.main_page.find(self.main_page.locators.PHONE_NUMBER_LOCATOR).get_attribute(
            'value')
        assert full_name == changed_full_name
        assert contact_phone_number == changed_contact_phone_number

    @pytest.mark.parametrize(
        'page_locator, item_locator',
        [
            pytest.param(
                MainPageLocators.PROFILE_LOCATOR, MainPageLocators.PROFILE_SETTINGS_LOCATOR
            ),
            pytest.param(
                MainPageLocators.AUDIENCES_LOCATOR, MainPageLocators.AUDIENCE_SEGMENTS_LOCATOR
            )
        ]
    )
    def test_go_to_page(self, page_locator, item_locator, login):
        self.main_page.click(page_locator)
        assert self.main_page.find(item_locator).is_displayed()
