from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED_TITLE = By.XPATH, './/h1[text()="Лента заказов"]'  # заголовок страницы Лента заказов
    ORDER_ITEM = By.XPATH, './/li[starts-with(@class, "OrderHistory_listItem")]'  # заказ
    COMPOUND_ORDER_TITLE = By.XPATH, ('.//div[starts-with(@class, "Modal_orderBox")]'
                                      '/p[starts-with(@class, "text text_type_main-medium")]')  # заголовок 'Состав' в модальном окне просмотра заказов
    ORDER_ID_IN_ORDER_FEED = By.XPATH, '//p[text()="{}"]'  # ID заказа в Ленте заказов
