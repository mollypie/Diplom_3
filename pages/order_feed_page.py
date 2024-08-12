import allure

from locators.order_feed_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Получение заголовка страницы Лента Заказов')
    def get_title_on_order_feed_page(self):
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_FEED_TITLE)