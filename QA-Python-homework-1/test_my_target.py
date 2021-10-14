import pytest
from base import BaseCase

class Test(BaseCase):
    @pytest.fixture(scope='function')
    def login(self):
        self.login_page.login()

    def test_login(self, login):
        assert self.driver.current_url == 'https://target.my.com/dashboard'
