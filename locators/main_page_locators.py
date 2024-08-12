from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_ACCOUNT = By.XPATH, './/a[starts-with(@class, "AppHeader_header") and @href="/account"]'  # кнопка Личный Кабинет
    MAIN_TITLE = By.XPATH, './/h1[text()="Соберите бургер"]'  # заголовок страницы Главная (конструктор)
