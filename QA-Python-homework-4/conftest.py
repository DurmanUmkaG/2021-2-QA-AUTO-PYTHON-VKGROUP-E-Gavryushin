import os.path

import pytest
from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--appium', default='127.0.0.1:4723/wd/hub')


@pytest.fixture(scope='session')
def config(request):
    appium = request.config.getoption('--appium')
    return {'appium': appium}


@pytest.fixture(scope='session')
def apk_path():
    return os.path.abspath(os.path.join(__file__, os.pardir, 'apk', 'Marussia_v1.50.2.apk'))
