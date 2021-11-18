from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class NumberOfRequests(Base):
    __tablename__ = 'number_of_requests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number_of_requests = Column(Integer, nullable=False)


class NumberOfRequestsByType(Base):
    __tablename__ = 'number_of_requests_by_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    request_type = Column(String(255), nullable=False)
    number_of_requests = Column(Integer, nullable=False)


class FrequentRequest(Base):
    __tablename__ = 'top_10_most_frequent_requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255), nullable=False)
    number_of_request = Column(Integer, nullable=False)


class BiggestSizeRequest(Base):
    __tablename__ = 'top_5_biggest_size_requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255), nullable=False)
    status_code = Column(Integer, nullable=False)
    request_size = Column(Integer, nullable=False)


class UserWithMaxNumberOfRequests(Base):
    __tablename__ = 'top_5_users_by_the_number_of_requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(40), nullable=False)
    number_of_request = Column(Integer, nullable=False)
