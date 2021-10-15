import pytest
from base import BaseCase


class Test(BaseCase):
    @pytest.fixture(scope='function')
    def login(self):
        self.login_page.login()

    @pytest.mark.skip
    def test_login(self, login):
        assert self.driver.current_url == 'https://target.my.com/dashboard'

    @pytest.mark.skip
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
