from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    LINK_TITLE = By.XPATH, './/div[starts-with(@class, "Auth_login")]/h2'  # заголовок страницы Восстановление пароля (новый пароль)
    SHOW_PASSWORD = By.XPATH, './/div[starts-with(@class, "input__icon")]'  # глазик показать/скрыть пароль
    INPUT_PASSWORD = By.XPATH, './/div[starts-with(@class, "input")]/input[starts-with(@class, "text")]'  # поле ввода пароля
