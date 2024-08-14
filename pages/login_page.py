import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Получение заголовка страницы Входа')
    def get_title_on_login_page(self):
        return self.get_text_from_element(LoginPageLocators.LOGIN_TITLE)

    @allure.step('Клик по ссылке Восстановить пароль на странице авторизации')
    def click_to_forgot_password_link(self):
        self.click_to_element(LoginPageLocators.LINK_FORGOT_PASSWORD)

    @allure.step('Ввод почты в поле')
    def enter_email(self, email):
        self.add_text_to_element(LoginPageLocators.INPUT_EMAIL, email)

    @allure.step('Ввод пароля в поле')
    def enter_password(self, password):
        self.add_text_to_element(LoginPageLocators.INPUT_PASSWORD, password)

    @allure.step('Клик на кнопку Войти')
    def click_to_button_enter(self):
        self.click_to_element(LoginPageLocators.BUTTON_ENTER)
