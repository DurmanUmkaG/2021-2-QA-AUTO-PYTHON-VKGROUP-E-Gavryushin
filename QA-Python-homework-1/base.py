import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = config.getfixturevalue('base_page')
