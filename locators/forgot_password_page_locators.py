from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    LINK_TITLE = By.XPATH, './/div[starts-with(@class, "Auth_login")]/h2'  # заголовок страницы Восстановление пароля

