import pytest
import requests
from selenium import webdriver

# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

from helpers import Helpers
from pages_url import *
from webdriver_factory import WebdriverFactory


# @pytest.fixture(params=['firefox', 'chrome'])
# def driver(request):
#     if request.param == 'firefox':
#         options = Options()
#         driver = webdriver.Firefox(options=options)
#     elif request.param == 'chrome':
#         driver = webdriver.Chrome()
#     yield driver
#     driver.quit()


# @pytest.fixture
# def user(driver):
#     ext_driver = WebdriverFactory.get_webdriver('firefox')
#
#     credentials = Helpers.generate_credentials(email=True, password=True, name=True)
#
#     create_user = requests.post(MAIN_PAGE + '/api/auth/register', data=credentials)
#     assert create_user.status_code == 200
#
#     yield {'driver': ext_driver, 'credentials': credentials}
#
#     requests.delete(MAIN_PAGE + '/api/auth/user', headers={'Authorization': create_user.json()['accessToken']})
#
#     ext_driver.quit()

@pytest.fixture(params=['chrome'])
def driver_wrapper(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        options = Options()
        driver = webdriver.Firefox(options=options)

    credentials = Helpers.generate_credentials(email=True, password=True, name=True)
    user = Helpers.create_user(credentials)

    yield driver, credentials

    Helpers.delete_user(user)

    driver.quit()
