#!/usr/bin/python
from common.Locators import HomePageLocators
from pageObjects.authenticationPage import AuthenticationPage
from pageObjects.basePageElement import BasePageElement


class HomePage(BasePageElement):

    def __init__(self, driver):
        self.driver = driver

    def clickOnSignInBtn(self):
        self.driver.find_element(*HomePageLocators.SIGNIN_BTN).click()
        return AuthenticationPage(self.driver)

    def clickOnContactBtn(self):
        self.driver.find_element(*HomePageLocators.CONTACT_BTN).click()

    def launchURL(self, url):
        self.driver.get(url)


