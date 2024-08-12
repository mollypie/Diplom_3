import allure

from conftest import user
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages_url import *


class TestAccountPage:
    @allure.title('Переход в раздел «История заказов»')
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
        account_page.click_to_order_history_element()
        profile = account_page.get_order_history_element()

        assert account_page.get_text_order_history_element() == 'История заказов' and profile.get_attribute('aria-current') == 'page'

    @allure.title('Выход из аккаунта')
    def test_logout(self, user):
        extended_driver = user['driver']
        extended_driver.get(LOGIN_PAGE)

        login_page = LoginPage(extended_driver)
        login_page.enter_email(user['credentials']['email'])
        login_page.enter_password(user['credentials']['password'])
        login_page.click_to_button_enter()

        main_page = MainPage(extended_driver)
        main_page.click_to_account_button()

        account_page = AccountPage(extended_driver)
        account_page.click_to_exit_element()

        login_page = LoginPage(extended_driver)

        assert login_page.get_title_on_login_page() == 'Вход'
