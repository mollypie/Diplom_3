from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_TITLE = By.XPATH, './/h1[text()="Соберите бургер"]'  # заголовок страницы Главная (конструктор)
    ACCOUNT_BUTTON = By.XPATH, './/a[starts-with(@class, "AppHeader_header") and @href="/account"]'  # кнопка Личный Кабинет
    ORDER_FEED_BUTTON = By.XPATH, './/p[text()="Лента Заказов"]/parent::a'  # кнопка Лента Заказов
    INGREDIENT_BUTTON = By.XPATH, './/a[starts-with(@class, "BurgerIngredient")]'  # Ингредиент
    INGREDIENT_DETAILS_MODAL_TITLE = By.XPATH, './/h2[text()="Детали ингредиента"]'  # заголовок модального окна Деталей заказа
