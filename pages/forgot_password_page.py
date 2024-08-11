import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Получение заголовка страницы восстановления пароля')
    def get_title_on_login_page(self):
        return self.get_text_from_element(ForgotPasswordPageLocators.LINK_TITLE)
