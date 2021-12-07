from dataclasses import dataclass

from faker import Faker

fake = Faker()


class Builder:

    def create_user(self, name=None, surname=None):

        @dataclass
        class User:
            name: str = None
            surname: str = None

        if name is None:
            name = fake.first_name()

        if surname is None:
            surname = fake.last_name()

        return User(name=name, surname=surname)
