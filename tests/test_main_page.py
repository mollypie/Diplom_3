import allure

from conftest import *
from data import *
from helpers import Helpers
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages_url import LOGIN_PAGE


class TestMainPage:
    @allure.title('Переход по клику на Личный кабинет')
    def test_open_account_page(self, driver, user):
        driver.get(LOGIN_PAGE)

        Helpers.login_user(driver, user)

        main_page = MainPage(driver)
        main_page.click_to_account_button()

        account_page = AccountPage(driver)

        assert (account_page.get_text_profile_element() == PROFILE_BUTTON
                and account_page.get_profile_element().get_attribute('aria-current') == 'page')

    @allure.title('Переход по клику в Лента Заказов')
    def test_open_order_feed_page(self, driver, user):
        driver.get(LOGIN_PAGE)

        Helpers.login_user(driver, user)

        main_page = MainPage(driver)
        main_page.click_to_order_feed_button()

        order_feed_page = OrderFeedPage(driver)

        assert order_feed_page.get_title_on_order_feed_page() == ORDER_FEED_PAGE_TITLE

    @allure.title('Открытие модального окна Детали ингредиента')
    def test_open_ingredient_details_modal(self, driver, user):
        driver.get(LOGIN_PAGE)

        Helpers.login_user(driver, user)

        main_page = MainPage(driver)
        main_page.click_to_ingredient()

        assert (main_page.get_title_on_ingredient_details_modal() == INGREDIENT_DETAILS_MODAL_TITLE
                and 'opened' in main_page.find_modal_window().get_attribute('class'))

    @allure.title('Закрытие модального окна Детали ингредиента')
    def test_close_ingredient_details_modal(self, driver, user):
        driver.get(LOGIN_PAGE)

        Helpers.login_user(driver, user)

        main_page = MainPage(driver)
        main_page.click_to_ingredient()

        main_page.click_to_close_modal_window()

        assert 'opened' not in main_page.find_modal_window().get_attribute('class')

    @allure.title('Подсчёт добавленного ингредиента')
    def test_count_ingredient(self, driver, user):
        driver.get(LOGIN_PAGE)

        Helpers.login_user(driver, user)

        main_page = MainPage(driver)
        main_page.add_ingredient_to_basket()

        assert main_page.get_ingredients_counter() == '2'

    @allure.title('Оформление заказа залогиненным пользователем')
    def test_create_order(self, driver, user):
        driver.get(LOGIN_PAGE)

        Helpers.login_user(driver, user)

        main_page = MainPage(driver)
        main_page.add_ingredient_to_basket()
        main_page.click_to_order_button()

        assert main_page.get_title_order_id_in_modal() == ORDER_ID_IN_MODAL_TITLE
