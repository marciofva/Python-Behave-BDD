#!/usr/bin/python
from common.Locators import LoginPageLocators
from pageObjects.accountPage import AccountPage
from pageObjects.basePageElement import BasePageElement


class AuthenticationPage(BasePageElement):

    def __init__(self, driver):
        self.driver = driver

    def clickOnCreateAccountBtn(self):
        self.driver.find_element(*LoginPageLocators.CREATE_ACCOUNT_BTN).click()
        return AccountPage(self.driver)

    def sendKeysSignUpEmail(self, email):
        self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)

    def getErrorMessage(self):
        return self.driver.find_element(*LoginPageLocators.EMAIL_ERROR).text