import allure
from selenium.webdriver.support.wait import WebDriverWait

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
        new_locator = self.format_locators(OrderFeedPageLocators.ORDER_ID_IN_ORDER_FEED, order_id)
        self.scroll_to_element(new_locator)
        return self.get_text_from_element(new_locator)

    @allure.step('Получение количества заказов за всё время')
    def get_all_orders_count(self):
        return self.get_text_from_element(OrderFeedPageLocators.COUNT_ORDER_ALL)

    @allure.step('Получение количества заказов за сегодня')
    def get_today_orders_count(self):
        return self.get_text_from_element(OrderFeedPageLocators.COUNT_ORDER_TODAY)

    @allure.step('Клик на кнопку Конструктор')
    def click_to_constructor_button(self):
        return self.click_to_element(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Получение идентификатора заказа в блоке "В работе"')
    def get_order_id_in_work(self, order_id):
        new_locator = self.format_locators(OrderFeedPageLocators.ORDER_ID_IN_WORK, order_id)
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*new_locator).text == f'0{order_id}'
        )
        return self.get_text_from_element(new_locator)
