import pytest
import requests

from helpers import Helpers
from pages_url import MAIN_PAGE
from webdriver_factory import WebdriverFactory


@pytest.fixture
def driver():
    driver = WebdriverFactory.get_webdriver('chrome')

    yield driver

    driver.quit()


@pytest.fixture
def user():
    credentials = Helpers.generate_credentials(email=True, password=True, name=True)
    requests.post(MAIN_PAGE + '/api/auth/register', data=credentials)

    new_user = requests.post(MAIN_PAGE + '/api/auth/login', data=Helpers.credentials_for_login(credentials))

    yield new_user

    requests.delete(MAIN_PAGE + '/api/auth/user', headers={'Authorization': new_user.json()['accessToken']})
