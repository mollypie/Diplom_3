import allure

from locators.order_feed_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Получение заголовка страницы Лента Заказов')
    def get_title_on_order_feed_page(self):
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_FEED_TITLE)

    @allure.step('Открытие детального просмотра заказа')
    def get_order_details_modal(self):
        return self.click_to_element(OrderFeedPageLocators.ORDER_ITEM)

    @allure.step('Получение заголовка "Состав" в модальном окне просмотра заказов')
    def get_title_on_order_details_modal(self):
        return self.get_text_from_element(OrderFeedPageLocators.COMPOUND_ORDER_TITLE)
