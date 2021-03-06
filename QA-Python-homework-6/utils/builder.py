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

    def create_number_of_requests_by_type(self, request_type, number_of_requests):
        number_of_requests_by_type = NumberOfRequestsByType(
            request_type=request_type,
            number_of_requests=number_of_requests
        )
        self.client.session.add(number_of_requests_by_type)
        self.client.session.commit()

        return number_of_requests_by_type

    def create_frequent_request(self, url, number_of_requests):
        frequent_request = FrequentRequest(
            url=url,
            number_of_requests=number_of_requests
        )

        self.client.session.add(frequent_request)
        self.client.session.commit()

        return frequent_request

    def create_biggest_size_request(self, url, status_code, request_size, ip):
        biggest_size_request = BiggestSizeRequest(
            url=url,
            status_code=status_code,
            request_size=request_size,
            ip=ip
        )

        self.client.session.add(biggest_size_request)
        self.client.session.commit()

    def create_user_with_max_number_of_request(self, ip, number_of_requests):
        user_with_max_number_of_request = UserWithMaxNumberOfRequests(
            ip=ip,
            number_of_requests=number_of_requests
        )

        self.client.session.add(user_with_max_number_of_request)
        self.client.session.commit()
