import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Получение заголовка страницы Главная (конструктор)')
    def get_title_on_main_page(self):
        return self.get_text_from_element(MainPageLocators.MAIN_TITLE)

    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_to_account_button(self):
        self.click_to_element(MainPageLocators.BUTTON_ACCOUNT)
