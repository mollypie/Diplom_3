import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Получение заголовка страницы восстановления пароля')
    def get_title_on_login_page(self):
        return self.get_text_from_element(ForgotPasswordPageLocators.LINK_TITLE)

    @allure.step('Ввод почты в поле')
    def enter_email(self, email):
        return self.add_text_to_element(ForgotPasswordPageLocators.INPUT_EMAIL, email)

    @allure.step('Клик по кнопке «Восстановить»')
    def click_recover_button(self):
        return self.click_to_element(ForgotPasswordPageLocators.RECOVER_BUTTON)
