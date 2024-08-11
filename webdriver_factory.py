from selenium import webdriver


class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == 'fireFox':
            return webdriver.Firefox()
        elif browser_name == 'chrome':
            return webdriver.Chrome()