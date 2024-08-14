import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Получение заголовка страницы Главная (конструктор)')
    def get_title_on_main_page(self):
        return self.get_text_from_element(MainPageLocators.MAIN_TITLE)

    @allure.step('Клик по кнопке Личный кабинет')
    def click_to_account_button(self):
        self.click_to_element(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step('Клик по кнопке Лента Заказов')
    def click_to_order_feed_button(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    # @allure.step('Получение ингредиента')
    # def get_ingredients(self):
    #     return self.get_text_from_element(MainPageLocators.INGREDIENT_BUTTON)

    @allure.step('Клик по ингредиенту')
    def click_to_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT_BUTTON)

    @allure.step('Поиск Модального окна Деталей заказа')
    def find_modal_window(self):
        return self.find_element_with_wait(MainPageLocators.MODAL_WINDOW)

    @allure.step('Получение заголовка модального окна Деталей заказа')
    def get_title_on_ingredient_details(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_DETAILS_MODAL_TITLE)

    @allure.step('Закрытие модального окна Деталей заказа')
    def click_to_close_modal_window(self):
        self.click_to_element(MainPageLocators.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step('Добавление ингредиента в корзину')
    def add_ingredient_to_basket(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT_R2_D3_BUN, MainPageLocators.CONSTRUCTOR_SECTION)

    @allure.step('Получение каунтера ингредиента')
    def get_ingredients_counter(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENTS_COUNTER)

    @allure.step('Клик по кнопке Оформить заказ')
    def click_to_order_button(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Получение заголовка Идентификатор заказа в модальном окне Заказа')
    def get_title_order_id(self):
        return self.get_text_from_element(MainPageLocators.ORDER_ID_TITLE)

    @allure.step('Ожидание присвоения идентификатора заказу в модальном окне Заказа')
    def wait_order_id(self):
        self.wait_element_with_non_condition(MainPageLocators.ORDER_ID_IN_MODAL, '9999')

    @allure.step('Получение идентификатора заказа в модальном окне Заказа')
    def get_order_id_in_modal(self):
        self.wait_element_with_non_condition(MainPageLocators.ORDER_ID_IN_MODAL, '9999')
        return self.get_text_from_element(MainPageLocators.ORDER_ID_IN_MODAL)

