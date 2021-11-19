from faker import Faker
from models.model import NumberOfRequests, NumberOfRequestsByType, FrequentRequest, BiggestSizeRequest, \
    UserWithMaxNumberOfRequests

fake = Faker()


class MysqlBuilder:
    def __init__(self, client):
        self.client = client

    def create_number_of_requests(self, number_of_request):
        number_of_requests = NumberOfRequests(
            number_of_requests=number_of_request
        )
        self.client.session.add(number_of_requests)
        self.client.session.commit()

        return number_of_requests
