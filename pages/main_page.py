import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_to_account_button(self):
        self.click_to_element(MainPageLocators.BUTTON_ACCOUNT)
