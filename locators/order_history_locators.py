from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    ORDER_ID_IN_HISTORY = By.XPATH, ('.//div[starts-with(@class, "OrderHistory_textBox")]'
                                     '/p[starts-with(@class, "text text_type_digits-default")]')  # ID заказа в Истории заказов
