import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание появления элемента на странице')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        self.wait_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Клик на элемент')
    def click_to_element(self, locator):
        self.wait_element(locator)
        self.driver.find_element(*locator).click()

    @allure.step('Ввод текста')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получение текста с элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Скролл')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
