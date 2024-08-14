import allure

from conftest import driver_wrapper
from data import *
from helpers import Helpers
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages_url import LOGIN_PAGE


class TestLoginPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке Восстановить пароль')
    def test_open_forgot_password_page(self, driver_wrapper):
        driver = Helpers.get_driver(driver_wrapper)
        driver.get(LOGIN_PAGE)

        login_page = LoginPage(driver)
        login_page.click_to_forgot_password_link()

        forgot_password_page = ForgotPasswordPage(driver)

        assert forgot_password_page.get_title_on_forgot_password_page() == PASSWORD_RECOVERY_TITLE
