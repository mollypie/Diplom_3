import pytest

from webdriver_factory import WebdriverFactory


@pytest.fixture
def driver():
    driver = WebdriverFactory.get_webdriver('chrome')

    yield driver

    driver.quit()
