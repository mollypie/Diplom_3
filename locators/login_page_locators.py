from selenium.webdriver.common.by import By


class LoginPageLocators:
    LINK_TITLE = By.XPATH, './/div[starts-with(@class, "Auth_login")]/h2'  # заголовок страницы Входа
    LINK_FORGOT_PASSWORD = By.XPATH, './/a[starts-with(@class, "Auth_link") and @href="/forgot-password"]'  # ссылка Восстановить пароль
    INPUT_EMAIL = By.NAME, 'name'  # поле Email
    INPUT_PASSWORD = By.NAME, 'Пароль'  # поле пароль
    BUTTON_ENTER = By.XPATH, './/button[starts-with(@class, "button_button")]'  # кнопка Войти
