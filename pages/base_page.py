import allure
from selenium.webdriver import ActionChains

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание появления элемента на странице')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание появления элемента на странице с условием неравенства')
    def wait_element_with_non_condition(self, locator, condition):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*locator).text != condition
        )

    @allure.step('Ожидание появления элемента на странице с условием равенства')
    def wait_element_with_condition(self, locator, condition):
        WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element(*locator).text == condition
        )

    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        self.wait_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Получение текста с элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Клик на элемент')
    def click_to_element(self, locator):
        self.wait_element(locator)
        self.driver.find_element(*locator).click()

    @allure.step('Ввод текста')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Скролл')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Drag and Drop')
    def drag_and_drop(self, draggable_locator, droppable_locator):
        draggable = self.find_element_with_wait(draggable_locator)
        start = draggable.location
        finish = self.find_element_with_wait(droppable_locator).location
        ActionChains(self.driver) \
            .drag_and_drop_by_offset(draggable, finish['x'] - start['x'], finish['y'] - start['y']) \
            .perform()

    @allure.step('Добавление значения локатору')
    def format_locators(self, locator, value):
        method, locator_new = locator
        locator_new = locator_new.format(value)

        return (method, locator_new)
