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
