import allure

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step('Получение текста с первого элемента функций аккаунта')
    def get_text_profile_element(self):
        return self.get_text_from_element(AccountPageLocators.FIRST_ELEMENT_OF_LIST)
