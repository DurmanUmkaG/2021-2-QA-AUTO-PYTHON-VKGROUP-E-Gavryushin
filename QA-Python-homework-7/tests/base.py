import pytest
from utils.builder import Builder


class BaseTest:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, http_client, logger):
        self.client = http_client
        self.logger = logger
        self.builder = Builder()

    @pytest.fixture(scope='function')
    def user(self):
        user = self.builder.create_user()
        self.add_user(user.name, user.surname)
        yield user
        self.delete_user_by_name(user.name)

    def add_user(self, name, surname):
        return self.client.post_add_user(name, surname)

    def get_user_by_name(self, name):
        return self.client.get_user_by_name(name)

    def delete_user_by_name(self, name):
        return self.client.delete_user_by_name(name)

    def update_user_by_name(self, name, surname):
        return self.client.put_update_user_by_name(name, surname)
