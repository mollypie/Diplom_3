import pytest
from selenium import webdriver

from helpers import Helpers


@pytest.fixture(params=['chrome'])  # , 'firefox'
def driver(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1280,720')
        driver = webdriver.Chrome(options=chrome_options)
    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--width=1280')
        firefox_options.add_argument('--height=720')
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise Exception("Invalid driver param")

    yield driver

    driver.quit()


@pytest.fixture
def user(driver):
    credentials = Helpers.generate_credentials(email=True, password=True, name=True)
    user = Helpers.create_user(credentials)

    yield credentials

    Helpers.delete_user(user)
