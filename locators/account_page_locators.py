from selenium.webdriver.common.by import By


class AccountPageLocators:
    FIRST_ELEMENT_OF_LIST = By.XPATH, './/a[text()="Профиль"]'  # первый элемент списка функций аккаунта
