from tests.base import BaseTest


class TestMock(BaseTest):
    def test_has_surname(self, user):
        self.add_user(user.name, user.surname)
        assert self.get_user(user.name) == user.surname

    def test_has_no_surname(self, user):
        assert 'not found' in self.get_user(user.name)