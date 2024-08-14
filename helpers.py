import random
import string

import requests

from pages.login_page import LoginPage
from pages_url import MAIN_PAGE


class Helpers:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_credentials(email=False, password=False, name=False):
        credentials = {}

        if email:
            credentials['email'] = Helpers.generate_random_email(6)

        if password:
            credentials['password'] = Helpers.generate_random_string(10)

        if name:
            credentials['name'] = Helpers.generate_random_string(10)

        return credentials

    @staticmethod
    def generate_random_email(num_email):
        email = Helpers.generate_random_string(num_email) + '@test.ts'

        return email

    @staticmethod
    def create_user(credentials):
        create_user = requests.post(MAIN_PAGE + '/api/auth/register', data=credentials)
        assert create_user.status_code == 200

        return create_user

    @staticmethod
    def delete_user(user):
        requests.delete(MAIN_PAGE + '/api/auth/user', headers={'Authorization': user.json()['accessToken']})

    @staticmethod
    def get_driver(wrapper):
        return wrapper[0]

    @staticmethod
    def get_creds(wrapper):
        return wrapper[1]

    @staticmethod
    def login_user(driver, credentials):
        login_page = LoginPage(driver)

        login_page.enter_email(credentials['email'])
        login_page.enter_password(credentials['password'])
        login_page.click_to_button_enter()

    @staticmethod
    def create_order(main_page):
        main_page.add_ingredient_to_basket()
        main_page.click_to_order_button()
        main_page.wait_order_id_in_modal()
        main_page.click_to_close_modal_window()

    @staticmethod
    def create_order_and_return_order_id(main_page):
        main_page.add_ingredient_to_basket()
        main_page.click_to_order_button()
        main_page.wait_order_id_in_modal()
        order_id = main_page.get_order_id_in_modal()
        main_page.click_to_close_modal_window()

        return order_id
