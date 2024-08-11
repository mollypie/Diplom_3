import random
import string


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
    def credentials_for_login(credentials):
        credentials_for_login = {
            'email': credentials['email'],
            'password': credentials['password']
        }

        return credentials_for_login
