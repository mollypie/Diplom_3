import allure

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step('Получение текста с элемента Профиль')
    def get_text_profile_element(self):
        return self.get_text_from_element(AccountPageLocators.PROFILE_ELEMENT)

    @allure.step('Получение элемента Профиль')
    def get_profile_element(self):
        return self.find_element_with_wait(AccountPageLocators.PROFILE_ELEMENT)

    @allure.step('Получение текста с элемента История заказов')
    def get_text_order_history_element(self):
        return self.get_text_from_element(AccountPageLocators.ORDER_HISTORY_ELEMENT)

    @allure.step('Получение элемента История заказов')
    def get_order_history_element(self):
        return self.find_element_with_wait(AccountPageLocators.ORDER_HISTORY_ELEMENT)

    @allure.step('Клик на элемент История заказов')
    def click_to_order_history_element(self):
        return self.click_to_element(AccountPageLocators.ORDER_HISTORY_ELEMENT)

    @allure.step('Клик на элемент Выход')
    def click_to_exit_element(self):
        return self.click_to_element(AccountPageLocators.EXIT_ELEMENT)

    @allure.step('Клик на кнопку Конструктор')
    def click_to_constructor_button(self):
        return self.click_to_element(AccountPageLocators.CONSTRUCTOR_BUTTON)
