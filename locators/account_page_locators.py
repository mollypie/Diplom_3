from selenium.webdriver.common.by import By


class AccountPageLocators:
    PROFILE_ELEMENT = By.XPATH, './/a[text()="Профиль"]'  # элемент Профиль в личном кабинете
    ORDER_HISTORY_ELEMENT = By.XPATH, './/a[text()="История заказов"]'  # элемент История заказов в личном кабинете
    EXIT_ELEMENT = By.XPATH, './/button[text()="Выход"]'  # элемент Выход в личном кабинете
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]/parent::a'  # кнопка Конструктор
    ORDER_FEED_BUTTON = By.XPATH, './/p[text()="Лента Заказов"]/parent::a'  # кнопка Лента Заказов
