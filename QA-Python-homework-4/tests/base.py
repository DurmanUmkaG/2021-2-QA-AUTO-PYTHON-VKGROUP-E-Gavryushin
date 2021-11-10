import pytest

from ui.pages.base_page import BasePage
from _pytest.fixtures import FixtureRequest


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver
        self.base_page: BasePage = request.getfixturevalue('base_page')
