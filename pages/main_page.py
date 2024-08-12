import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Получение заголовка страницы Главная (конструктор)')
    def get_title_on_main_page(self):
        return self.get_text_from_element(MainPageLocators.MAIN_TITLE)

    @allure.step('Клик по кнопке «Личный кабинет»')
    def click_to_account_button(self):
        self.click_to_element(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step('Клик по кнопке «Лента Заказов»')
    def click_to_order_feed_button(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Клик по Ингредиенту')
    def click_to_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT_BUTTON)

    @allure.step('Получение заголовка модального окна Деталей заказа')
    def get_title_on_ingredient_details(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_DETAILS_MODAL_TITLE)

    @allure.step('Поиск Модального окна')
    def find_modal_window(self):
        return self.find_element_with_wait(MainPageLocators.MODAL_WINDOW)

    @allure.step('Закрытие модального окна Деталей заказа')
    def click_to_close_modal_window(self):
        self.click_to_element(MainPageLocators.CLOSE_MODAL_WINDOW_BUTTON)
