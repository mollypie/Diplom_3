from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED_TITLE = By.XPATH, './/h1[text()="Лента заказов"]'  # заголовок страницы Лента заказов
    ORDER_ITEM = By.XPATH, './/li[starts-with(@class, "OrderHistory_listItem")]'  # заказ
    COMPOUND_ORDER_TITLE = By.XPATH, ('.//div[starts-with(@class, "Modal_orderBox")]'
                                      '/p[starts-with(@class, "text text_type_main-medium")]')  # заголовок 'Состав' в модальном окне просмотра заказов
    ORDER_ID_IN_ORDER_FEED = By.XPATH, '//p[text()="{}"]'  # ID заказа в Ленте заказов
    ORDER_ID_IN_WORK = By.XPATH, ('.//ul[starts-with(@class, "OrderFeed_orderListReady")]'
                                  '/li[contains(normalize-space(.), "{}")]')  # заказы "В работе"
    COUNT_ORDER_ALL = By.XPATH, ('.//p[text()="Выполнено за все время:"]'
                                 '/parent::div'
                                 '/p[starts-with(@class, "OrderFeed_number")]')  # количество заказов за всё время
    COUNT_ORDER_TODAY = By.XPATH, ('.//p[text()="Выполнено за сегодня:"]'
                                   '/parent::div'
                                   '/p[starts-with(@class, "OrderFeed_number")]')  # количество заказов за сегодня
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]/parent::a'  # кнопка Конструктор
