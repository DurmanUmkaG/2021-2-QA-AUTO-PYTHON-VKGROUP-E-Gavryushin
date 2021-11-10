import random

import pytest

from ui.pages.base_page import BasePage
from _pytest.fixtures import FixtureRequest

from ui.pages.main_page import MainPage


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')

    @staticmethod
    def create_random_expression():
        number1, number2 = random.randint(0, 100), random.randint(0, 100)
        return {'number1': number1, 'number2': number2, 'result': number1 + number2}
