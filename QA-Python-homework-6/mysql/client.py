import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

from models.model import Base


class MysqlClient:
    def __init__(self, user, password, db_name, host, port):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = host
        self.port = port

        self.engine = None
        self.connection = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        self.engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}',
            encoding='utf8'
        )
        self.connection = self.engine.connect()

        self.session = sessionmaker(bind=self.connection.engine)()

    def recreate_db(self):
        self.connect(db_created=False)

        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)

        self.connection.close()
        self.connect(db_created=True)

    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def create_table(self, table_name):
        if not inspect(self.engine).has_table(table_name):
            Base.metadata.tables[table_name].create(self.engine)
