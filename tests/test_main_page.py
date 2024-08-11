import allure

from conftest import user
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
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

        assert account_page.get_text_profile_element() == 'Профиль'
