import pytest
import requests

from helpers import Helpers
from pages_url import *
from webdriver_factory import WebdriverFactory


@pytest.fixture
def driver():
    driver = WebdriverFactory.get_webdriver('chrome')

    yield driver

    driver.quit()


@pytest.fixture
def user():
    ext_driver = WebdriverFactory.get_webdriver('chrome')

    credentials = Helpers.generate_credentials(email=True, password=True, name=True)

    create_user = requests.post(MAIN_PAGE + '/api/auth/register', data=credentials)
    assert create_user.status_code == 200

    yield {'driver': ext_driver, 'credentials': credentials}

    requests.delete(MAIN_PAGE + '/api/auth/user', headers={'Authorization': create_user.json()['accessToken']})

    ext_driver.quit()
