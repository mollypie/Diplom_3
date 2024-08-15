import allure

from conftest import *
from data import *
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestAccountPage:
    @allure.title('Переход в раздел История заказов')
    def test_open_order_history_page(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login_user(user)

        main_page = MainPage(driver)
        main_page.click_to_account_button()

        account_page = AccountPage(driver)
        account_page.click_to_order_history_element()

        assert (account_page.get_text_order_history_element() == ORDER_HISTORY_BUTTON
                and account_page.get_order_history_element().get_attribute('aria-current') == 'page')

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login_user(user)

        main_page = MainPage(driver)
        main_page.click_to_account_button()

        account_page = AccountPage(driver)
        account_page.click_to_exit_element()

        assert login_page.get_title_on_login_page() == LOGIN_PAGE_TITLE

    @allure.title('Переход по клику на Конструктор')
    def test_open_main_page(self, driver, user):
        login_page = LoginPage(driver)
        login_page.login_user(user)

        main_page = MainPage(driver)
        main_page.click_to_account_button()

        account_page = AccountPage(driver)
        account_page.click_to_constructor_button()

        assert main_page.get_title_on_main_page() == MAIN_PAGE_TITLE
