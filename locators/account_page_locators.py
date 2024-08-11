from selenium.webdriver.common.by import By


class AccountPageLocators:
    PROFILE_ELEMENT = By.XPATH, './/a[text()="Профиль"]'  # элемент Профиль в личном кабинете
    ORDER_HISTORY_ELEMENT = By.XPATH, './/a[text()="История заказов"]'  # элемент История заказов в личном кабинете
