from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    FORGOT_PASSWORD_TITLE = By.XPATH, './/div[starts-with(@class, "Auth_login")]/h2'  # заголовок страницы Восстановление пароля
    INPUT_EMAIL = By.XPATH, './/div[starts-with(@class, "input")]/input[starts-with(@class, "text")]'  # поле Email
    RECOVER_BUTTON = By.XPATH, './/button[starts-with(@class, "button_button") and text()="Восстановить"]'  # кнопка Восстановить
