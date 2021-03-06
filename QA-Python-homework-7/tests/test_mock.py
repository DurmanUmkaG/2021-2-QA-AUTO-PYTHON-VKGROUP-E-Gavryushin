from tests.base import BaseTest


class TestMock(BaseTest):
    def test_has_surname(self, user):
        assert self.get_user_by_name(user.name) == user.surname

    def test_has_no_surname(self):
        assert 'not found' in self.get_user_by_name(self.builder.create_user().name)

    def test_delete_existing_user(self):
        user = self.builder.create_user()
        self.add_user(user.name, user.surname)
        assert self.delete_user_by_name(user.name)[user.name] == user.surname
        assert 'not found' in self.get_user_by_name(user.name)

    def test_delete_non_existent_user(self):
        assert 'not found' in self.delete_user_by_name(self.builder.create_user().name)

    def test_update_existing_user_surname(self, user):
        new_user = self.builder.create_user()
        assert self.update_user_by_name(user.name, new_user.surname)[user.name] == new_user.surname

    def test_update_non_existent_user_surname(self):
        user = self.builder.create_user()
        assert 'not found' in self.update_user_by_name(user.name, user.surname)
