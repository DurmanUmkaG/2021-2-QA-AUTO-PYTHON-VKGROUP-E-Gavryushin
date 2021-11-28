import pytest
from utils.builder import Builder


class BaseTest():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, http_client, logger):
        self.client = http_client
        self.logger = logger
        self.builder = Builder()

    @pytest.fixture(scope='function')
    def user(self):
        return self.builder.create_user()

    def add_user(self, name, surname):
        return self.client.post_add_user(name, surname)

    def get_user(self, name):
        return self.client.get_user(name)
