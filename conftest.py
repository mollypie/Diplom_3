import pytest
from selenium import webdriver

from selenium.webdriver.firefox.options import Options

from helpers import Helpers


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
