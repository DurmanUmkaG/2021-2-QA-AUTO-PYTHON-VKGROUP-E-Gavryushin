import time
from tests.base import BaseCase


class Test(BaseCase):
    def test_population(self):
        assert '146' in self.main_page.get_population()
