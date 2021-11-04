import faker
import pytest


class ApiBase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, logger):
        self.api_client = api_client
        self.logger = logger
        self.faker = faker.Faker()

        if self.authorize:
            self.api_client.post_login()

    def create_segment(self):
        res = self.api_client.post_create_segment(self.faker.lexify('?' * 7))
        return res['id']

    def get_segments(self):
        res = self.api_client.get_segments()
        return list(map(lambda x: x['id'], res['items']))

    def delete_segment(self, segment_id):
        res = self.api_client.post_delete_segments(segment_id)
        return res['successes'][0]['source_id']
