import allure

from conftest import driver_wrapper
from data import *
from helpers import Helpers
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages_url import *


class TestAccountPage:
    @allure.title('Переход в раздел История заказов')
    def test_open_order_history_page(self, driver_wrapper):
        driver = Helpers.get_driver(driver_wrapper)
        driver.get(LOGIN_PAGE)

        Helpers.login_user(*driver_wrapper)

        main_page = MainPage(driver)
        main_page.click_to_account_button()

        account_page = AccountPage(driver)
        account_page.click_to_order_history_element()

        assert (account_page.get_text_order_history_element() == ORDER_HISTORY_BUTTON
                and account_page.get_order_history_element().get_attribute('aria-current') == 'page')

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver_wrapper):
        driver = Helpers.get_driver(driver_wrapper)
        driver.get(LOGIN_PAGE)

        Helpers.login_user(*driver_wrapper)

        main_page = MainPage(driver)
        main_page.click_to_account_button()

        account_page = AccountPage(driver)
        account_page.click_to_exit_element()

        login_page = LoginPage(driver)

        assert login_page.get_title_on_login_page() == LOGIN_PAGE_TITLE

    @allure.title('Переход по клику на Конструктор')
    def test_open_main_page(self, driver_wrapper):
        driver = Helpers.get_driver(driver_wrapper)
        driver.get(LOGIN_PAGE)

        Helpers.login_user(*driver_wrapper)

        main_page = MainPage(driver)
        main_page.click_to_account_button()

        account_page = AccountPage(driver)
        account_page.click_to_constructor_button()

        assert main_page.get_title_on_main_page() == MAIN_PAGE_TITLE
