import script
from models.model import NumberOfRequests, NumberOfRequestsByType, FrequentRequest, BiggestSizeRequest, \
    UserWithMaxNumberOfRequests
from tests.base import MysqlBase


class TestMysqlNumberOfRequests(MysqlBase):
    def prepare(self):
        self.mysql_builder.create_number_of_requests(
            script.get_total_number_of_requests(self.data)['total_number_of_requests'])

    def test_number_of_requests(self):
        assert self.get_numbers_of_rows_in_table(NumberOfRequests) == len(
            script.get_total_number_of_requests(self.data))


class TestMysqlNumberOfRequestsByType(MysqlBase):
    def prepare(self):
        for key, value in script.get_total_number_of_requests_by_type(self.data).items():
            self.mysql_builder.create_number_of_requests_by_type(key, value)

    def test_number_of_requests_by_type(self):
        assert self.get_numbers_of_rows_in_table(NumberOfRequestsByType) == len(
            script.get_total_number_of_requests_by_type(self.data))


class TestMysqlTop10MostFrequentRequests(MysqlBase):
    def prepare(self):
        for i in script.get_top_10_most_frequent_requests(self.data):
            self.mysql_builder.create_frequent_request(
                url=i['url'],
                number_of_requests=i['number_of_requests']
            )

    def test_top10_most_frequent_requests(self):
        assert self.get_numbers_of_rows_in_table(FrequentRequest) == len(
            script.get_top_10_most_frequent_requests(self.data))
