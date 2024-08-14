import allure

from conftest import driver_wrapper
from data import *
from helpers import Helpers
from pages.forgot_password_page import ForgotPasswordPage
from pages_url import FORGOT_PASSWORD_PAGE


class TestForgotPasswordPage:
    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_click_button(self, driver_wrapper):
        driver = Helpers.get_driver(driver_wrapper)
        driver.get(FORGOT_PASSWORD_PAGE)
        forgot_password_page = ForgotPasswordPage(driver)

        forgot_password_page.enter_email(Helpers.generate_random_email(6))
        forgot_password_page.click_recover_button()

        reset_password_page = ForgotPasswordPage(driver)

        assert reset_password_page.get_title_on_login_page() == TITLE_RECOVERY_PASSWORD
