import allure

from conftest import driver
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from pages_url import FORGOT_PASSWORD_PAGE


class TestResetPasswordPage:
    @allure.title('Активация поля нового пароля кликом по кнопке показать/скрыть пароль')
    def test_click_to_show_password(self, driver):
        driver.get(FORGOT_PASSWORD_PAGE)

        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.click_recover_button()

        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.click_recover_and_hide_button()

        assert reset_password_page.find_password_input().get_attribute('type') == 'text'
