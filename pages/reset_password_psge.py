import allure

from locators.reset_password_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step('Получение заголовка страницы нового пароля')
    def get_title_on_reset_page(self):
        return self.get_text_from_element(ResetPasswordPageLocators.LINK_TITLE)
