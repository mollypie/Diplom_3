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

    @allure.step('Получение заголовка "Состав" в модальном окне просмотра заказов')
    def get_title_on_order_details_modal(self):
        return self.get_text_from_element(OrderFeedPageLocators.COMPOUND_ORDER_TITLE)

    @allure.step('Получение ID заказа в Ленте заказов')
    def get_order_id_in_order_feed_page(self, order_id):
        new_answer_locator = self.format_locators(OrderFeedPageLocators.ORDER_ID_IN_ORDER_FEED, order_id)
        self.scroll_to_element(new_answer_locator)
        return self.get_text_from_element(new_answer_locator)
