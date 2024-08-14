import allure

from locators.order_history_locators import OrderHistoryPageLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):
    @allure.step('Получение ID заказа в Истории заказов')
    def get_order_id_in_order_history_page(self):
        return self.get_text_from_element(OrderHistoryPageLocators.ORDER_ID_IN_HISTORY)
