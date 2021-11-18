import pytest

from mysql.client import MysqlClient


def pytest_addoption(parser):
    parser.addoption('--log_path', default='access.log')


@pytest.fixture(scope='session')
def config(request):
    log_path = request.config.getoption('--log_path')
    return {'log_path': log_path}


def pytest_configure(config):
    mysql_client = MysqlClient(
        user='root',
        password='pass',
        db_name='TEST_SQL',
        host='127.0.0.1',
        port=3307
    )
    if not hasattr(config, 'workerinput'):
        mysql_client.recreate_db()
        mysql_client.create_table('number_of_requests')
        mysql_client.create_table('number_of_requests_by_type')
        mysql_client.create_table('top_10_most_frequent_requests')
        mysql_client.create_table('top_5_biggest_size_requests')
        mysql_client.create_table('top_5_users_by_the_number_of_requests')
        mysql_client.connection.close()

    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> MysqlClient:
    client = request.config.mysql_client
    client.connect(db_created=True)
    yield client
    client.connection.close()
