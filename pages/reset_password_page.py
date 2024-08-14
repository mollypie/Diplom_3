import allure

from locators.reset_password_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step('Получение заголовка страницы нового пароля')
    def get_title_on_reset_page(self):
        return self.get_text_from_element(ResetPasswordPageLocators.RESET_PASSWORD_TITLE)

    @allure.step('Поиск поля ввода пароля')
    def find_password_input(self):
        return self.find_element_with_wait(ResetPasswordPageLocators.INPUT_PASSWORD)

    @allure.step('Клик по кнопке показать/скрыть пароль')
    def click_recover_and_hide_button(self):
        self.click_to_element(ResetPasswordPageLocators.SHOW_PASSWORD)
