import allure

from conftest import driver
from data import *
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages_url import LOGIN_PAGE


class TestLoginPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_open_forgot_password_page(self, driver):
        driver.get(LOGIN_PAGE)
        login_page = LoginPage(driver)
        login_page.click_to_forgot_password_link()

        forgot_password_page = ForgotPasswordPage(driver)

        assert forgot_password_page.get_title_on_login_page() == TITLE_RECOVERY_PASSWORD
