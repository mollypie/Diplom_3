import allure

from conftest import user
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages_url import LOGIN_PAGE


class TestMainPage:
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_open_account_page(self, user):
        extended_driver = user['driver']
        extended_driver.get(LOGIN_PAGE)

        login_page = LoginPage(extended_driver)
        login_page.enter_email(user['credentials']['email'])
        login_page.enter_password(user['credentials']['password'])
        login_page.click_to_button_enter()

        main_page = MainPage(extended_driver)
        main_page.click_to_account_button()

        account_page = AccountPage(extended_driver)
        profile = account_page.get_profile_element()

        assert account_page.get_text_profile_element() == 'Профиль' and profile.get_attribute('aria-current') == 'page'

    @allure.title('Переход по клику в «Лента Заказов»')
    def test_open_order_feed_page(self, user):
        extended_driver = user['driver']
        extended_driver.get(LOGIN_PAGE)

        login_page = LoginPage(extended_driver)
        login_page.enter_email(user['credentials']['email'])
        login_page.enter_password(user['credentials']['password'])
        login_page.click_to_button_enter()

        main_page = MainPage(extended_driver)
        main_page.click_to_order_feed_button()

        order_feed_page = OrderFeedPage(extended_driver)

        assert order_feed_page.get_title_on_order_feed_page() == 'Лента заказов'
