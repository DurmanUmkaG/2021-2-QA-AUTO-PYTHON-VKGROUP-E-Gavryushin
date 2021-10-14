import pytest
from base import BaseCase


class Test(BaseCase):
    @pytest.fixture(scope='function')
    def login(self):
        self.login_page.login()

    @pytest.mark.skip
    def test_login(self, login):
        assert self.driver.current_url == 'https://target.my.com/dashboard'

    def test_logout(self, login):
        self.main_page.logout()
        assert self.driver.current_url == 'https://target.my.com/'
