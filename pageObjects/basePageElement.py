from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class BasePageElement(object):

    def select_browser(self, browser):
        if 'chrome' in browser:
            driver = webdriver.Chrome()

        if 'firefox' in browser:
            driver = webdriver.Firefox()

        driver.implicitly_wait(10)
        return driver

    def elementIsPresent(self, *locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False