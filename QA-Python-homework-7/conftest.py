import logging
import os
import shutil
import sys
import time
from logging.handlers import RotatingFileHandler

import pytest
import requests
from werkzeug.serving import WSGIRequestHandler

import settings
from http_client.http_client import HTTPClient
from mock import flask_mock
from requests import ConnectionError

BASE_TIMEOUT = 5


def redirect_flask_output_to_log():
    # Redirect stdout and stderr to files
    info_handler = RotatingFileHandler(os.path.join(get_base_dir(), 'mock_stdout.log'), backupCount=1)
    info_handler.setLevel(logging.INFO)

    error_handler = RotatingFileHandler(os.path.join(get_base_dir(), 'mock_stderr.log'), backupCount=1)
    error_handler.setLevel(logging.ERROR)

    logging.root.handlers = [info_handler, error_handler]
    WSGIRequestHandler.protocol_version = "HTTP/1.1"


def get_base_dir():
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    return base_dir


def run_mock():
    redirect_flask_output_to_log()
    flask_mock.run_mock()
    wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)


def shutdown_mock():
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')


def wait_ready(host, port, timeout=BASE_TIMEOUT):
    started = False
    st = time.time()
    while time.time() - st <= timeout:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError(f'{host}:{port} did not started in 5s!')


def pytest_configure(config):
    base_dir = get_base_dir()

    if not hasattr(config, 'workerinput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)

        os.makedirs(base_dir)
        run_mock()
    config.base_temp_dir = base_dir


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        shutdown_mock()


@pytest.fixture(scope='function')
def logger(temp_dir):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(temp_dir, 'test.log')
    log_level = logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()


@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(
        request.config.base_temp_dir,
        request._pyfuncitem.nodeid.replace('/', '_').replace(':', '/')
    )

    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='function')
def http_client():
    client = HTTPClient(settings.MOCK_HOST, settings.MOCK_PORT)

    yield client

    client.close_connection()
