import allure

from conftest import user
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
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
