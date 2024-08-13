from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_TITLE = By.XPATH, './/h1[text()="Соберите бургер"]'  # заголовок страницы Главная (конструктор)
    ACCOUNT_BUTTON = By.XPATH, './/a[starts-with(@class, "AppHeader_header") and @href="/account"]'  # кнопка Личный Кабинет
    ORDER_FEED_BUTTON = By.XPATH, './/p[text()="Лента Заказов"]/parent::a'  # кнопка Лента Заказов
    INGREDIENT_BUTTON = By.XPATH, './/a[starts-with(@class, "BurgerIngredient")]'  # ингредиент
    INGREDIENT_DETAILS_MODAL_TITLE = By.XPATH, './/h2[text()="Детали ингредиента"]'  # заголовок модального окна Деталей заказа
    MODAL_WINDOW = By.XPATH, './/section[starts-with(@class, "Modal_modal")]'  # модальное окно Деталей заказа
    CLOSE_MODAL_WINDOW_BUTTON = By.XPATH, ('.//section[starts-with(@class, "Modal_modal_opened")]'
                                           '/div[starts-with(@class, "Modal_modal__container")]'
                                           '/button[@type="button"]')  # кнопка закрытия модального окна Деталей заказа
    INGREDIENT_R2_D3_BUN = By.XPATH, './/p[text()="Флюоресцентная булка R2-D3"]'  # ингредиент 'Флюоресцентная булка R2-D3'
    INGREDIENTS_COUNTER = By.XPATH, ('.//p[text()="Флюоресцентная булка R2-D3"]'
                                     '/parent::a'
                                     '/div[starts-with(@class, "counter_counter")]'
                                     '/p')  # каунтер ингредиента 'Флюоресцентная булка R2-D3'
    CONSTRUCTOR_SECTION = By.XPATH, './/section[starts-with(@class, "BurgerConstructor_basket")]'  # корзина заказа
