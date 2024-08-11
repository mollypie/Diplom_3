import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Клик по ссылке "Восстановить пароль" на странице авторизации')
    def click_to_forgot_password_link(self):
        self.click_to_element(LoginPageLocators.LINK_FORGOT_PASSWORD)







