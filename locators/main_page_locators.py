from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_TITLE = By.XPATH, './/h1[text()="Соберите бургер"]'  # заголовок страницы Главная (конструктор)
    BUTTON_ACCOUNT = By.XPATH, './/a[starts-with(@class, "AppHeader_header") and @href="/account"]'  # кнопка Личный Кабинет
    BUTTON_ORDER_FEED = By.XPATH, './/p[text()="Лента Заказов"]/parent::a'  # кнопка Лента Заказов
