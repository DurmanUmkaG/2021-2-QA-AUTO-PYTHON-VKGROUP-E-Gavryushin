import pytest

from mysql.client import MysqlClient
import script
from utils.builder import MysqlBuilder


class MysqlBase:
    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client, config):
        self.mysql_client: MysqlClient = mysql_client
        self.data = script.get_data_from_file(config['log_path'])
        self.mysql_builder: MysqlBuilder = MysqlBuilder(self.mysql_client)

        self.prepare()

    def get_numbers_of_rows_in_table(self, table):
        self.mysql_client.session.commit()
        return self.mysql_client.session.query(table).count()
