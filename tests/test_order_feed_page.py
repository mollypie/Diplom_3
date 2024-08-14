import allure

from conftest import user
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.order_history_page import OrderHistoryPage
from pages_url import LOGIN_PAGE


class TestOrderFeedPage:
    @allure.title('Получение всплывающего окна с деталями заказа')
    def test_open_order_details_modal(self, user):
        extended_driver = user['driver']
        extended_driver.get(LOGIN_PAGE)

        login_page = LoginPage(extended_driver)
        login_page.enter_email(user['credentials']['email'])
        login_page.enter_password(user['credentials']['password'])
        login_page.click_to_button_enter()

        main_page = MainPage(extended_driver)
        main_page.click_to_order_feed_button()

        order_feed_page = OrderFeedPage(extended_driver)
        order_feed_page.get_order_details_modal()

        assert order_feed_page.get_title_on_order_details_modal() == 'Cостав'

    @allure.title('Заказ пользователя из раздела «История заказов» отображается на странице «Лента заказов»')
    def test_order_details_modal(self, user):
        extended_driver = user['driver']
        extended_driver.get(LOGIN_PAGE)

        login_page = LoginPage(extended_driver)
        login_page.enter_email(user['credentials']['email'])
        login_page.enter_password(user['credentials']['password'])
        login_page.click_to_button_enter()

        main_page = MainPage(extended_driver)
        main_page.add_ingredient_to_basket()
        main_page.click_to_order_button()
        main_page.wait_order_id()
        main_page.click_to_close_modal_window()
        main_page.click_to_account_button()

        account_page = AccountPage(extended_driver)
        account_page.click_to_order_history_element()

        order_history_page = OrderHistoryPage(extended_driver)
        order_id = order_history_page.get_order_id_in_order_history_page()

        main_page.click_to_order_feed_button()

        order_feed_page = OrderFeedPage(extended_driver)

        assert order_feed_page.get_order_id_in_order_feed_page(order_id) == order_id

    @allure.title('Увеличение счётчика "Выполнено за всё время" при создании нового заказа')
    def test_increase_counter_all_time(self, user):
        extended_driver = user['driver']
        extended_driver.get(LOGIN_PAGE)

        login_page = LoginPage(extended_driver)
        login_page.enter_email(user['credentials']['email'])
        login_page.enter_password(user['credentials']['password'])
        login_page.click_to_button_enter()

        main_page = MainPage(extended_driver)
        main_page.click_to_order_feed_button()

        order_feed_page = OrderFeedPage(extended_driver)
        old_count = order_feed_page.get_all_orders_count()
        order_feed_page.click_to_constructor_button()

        main_page.add_ingredient_to_basket()
        main_page.click_to_order_button()
        main_page.wait_order_id()
        main_page.click_to_close_modal_window()
        main_page.click_to_order_feed_button()

        assert order_feed_page.get_all_orders_count() > old_count

    @allure.title('Увеличение счётчика "Выполнено за сегодня" при создании нового заказа')
    def test_increase_counter_all_time(self, user):
        extended_driver = user['driver']
        extended_driver.get(LOGIN_PAGE)

        login_page = LoginPage(extended_driver)
        login_page.enter_email(user['credentials']['email'])
        login_page.enter_password(user['credentials']['password'])
        login_page.click_to_button_enter()

        main_page = MainPage(extended_driver)
        main_page.click_to_order_feed_button()

        order_feed_page = OrderFeedPage(extended_driver)
        old_count = order_feed_page.get_today_orders_count()
        order_feed_page.click_to_constructor_button()

        main_page.add_ingredient_to_basket()
        main_page.click_to_order_button()
        main_page.wait_order_id()
        main_page.click_to_close_modal_window()
        main_page.click_to_order_feed_button()

        assert order_feed_page.get_today_orders_count() > old_count

    @allure.title('Заказ пользователя появляется в разделе "В работе"')
    def test_order_in_work(self, user):
        extended_driver = user['driver']
        extended_driver.get(LOGIN_PAGE)

        login_page = LoginPage(extended_driver)
        login_page.enter_email(user['credentials']['email'])
        login_page.enter_password(user['credentials']['password'])
        login_page.click_to_button_enter()

        main_page = MainPage(extended_driver)
        main_page.add_ingredient_to_basket()
        main_page.click_to_order_button()
        main_page.wait_order_id()
        order_id = main_page.get_order_id_in_modal()
        main_page.click_to_close_modal_window()
        main_page.click_to_order_feed_button()

        order_feed_page = OrderFeedPage(extended_driver)

        assert order_feed_page.get_order_id_in_work(order_id) == f'0{order_id}'
