from selenium.webdriver.support.select import Select

from common.Locators import AccountPageLocators
from pageObjects.basePageElement import BasePageElement
from pageObjects.myPersonalAccount import MyPersonalAccount


class AccountPage(BasePageElement):

    def __init__(self, driver):
        self.driver = driver

    def fillFormOut(self, name, value):

        if 'title' == name.lower():
            if 'mr' in value.lower():
                self.driver.find_element(*AccountPageLocators.TITLE_MR_RADIO).click()
            elif 'mrs' in value.lower():
                self.driver.find_element(*AccountPageLocators.TITLE_MRS_RADIO).click()

        if 'customer first name' == name.lower():
            self.driver.find_element(*AccountPageLocators.CUSTOMER_FIRST_NAME_FIELD).clear()
            self.driver.find_element(*AccountPageLocators.CUSTOMER_FIRST_NAME_FIELD).send_keys(value)

        if 'customer last name' == name.lower():
            self.driver.find_element(*AccountPageLocators.CUSTOMER_LAST_NAME_FIELD).clear()
            self.driver.find_element(*AccountPageLocators.CUSTOMER_LAST_NAME_FIELD).send_keys(value)

        if 'password' == name.lower():
            self.driver.find_element(*AccountPageLocators.PASSWORD_FIELD).clear()
            self.driver.find_element(*AccountPageLocators.PASSWORD_FIELD).send_keys(value)

        if 'day' == name.lower():
            mySelect = Select(self.driver.find_element(*AccountPageLocators.DAY_DROPDOWN))
            mySelect.select_by_value(value)

        if 'month' == name.lower():
            mySelect = Select(self.driver.find_element(*AccountPageLocators.MONTH_DROPDOWN))
            mySelect.select_by_value(value)

        if 'year' == name.lower():
            mySelect = Select(self.driver.find_element(*AccountPageLocators.YEAR_DROPDOWN))
            mySelect.select_by_value(value)

        if 'newsletter' == name.lower():
            if 'yes' in value.lower():
                self.driver.find_element(*AccountPageLocators.NEWSLETTER_CHECKBOX).click()

        if 'special offers' == name.lower():
            if 'yes' in value.lower():
                self.driver.find_element(*AccountPageLocators.OPTION_CHECKBOX).click()

        if 'first name' == name.lower():
            self.driver.find_element(*AccountPageLocators.FIRST_NAME_FIELD).clear()
            self.driver.find_element(*AccountPageLocators.FIRST_NAME_FIELD).send_keys(value)

        if 'last name' == name.lower():
            self.driver.find_element(*AccountPageLocators.LAST_NAME_FIELD).clear()
            self.driver.find_element(*AccountPageLocators.LAST_NAME_FIELD).send_keys(value)

        if 'company' == name.lower():
            self.driver.find_element(*AccountPageLocators.COMPANY_FIELD).clear()
            self.driver.find_element(*AccountPageLocators.COMPANY_FIELD).send_keys(value)

        if 'address' == name.lower():
            self.driver.find_element(*AccountPageLocators.ADDRESS_FIELD).clear()
            self.driver.find_element(*AccountPageLocators.ADDRESS_FIELD).send_keys(value)

        if 'city' == name.lower():
            self.driver.find_element(*AccountPageLocators.CITY_FIELD).clear()
            self.driver.find_element(*AccountPageLocators.CITY_FIELD).send_keys(value)

        if 'state' == name.lower():
            mySelect = Select(self.driver.find_element(*AccountPageLocators.STATE_DROPDOWN))
            mySelect.select_by_visible_text(value)

        if 'postcode' == name.lower():
            self.driver.find_element(*AccountPageLocators.POSTCODE_FIELD).clear()
            self.driver.find_element(*AccountPageLocators.POSTCODE_FIELD).send_keys(value)

        if 'country' == name.lower():
            mySelect = Select(self.driver.find_element(*AccountPageLocators.COUNTRY_DROPDOWN))
            if 'empty' in value.lower():
                mySelect.select_by_value("")
            else:
                mySelect.select_by_visible_text(value)

        if 'mobile' == name.lower():
            self.driver.find_element(*AccountPageLocators.MOBILE_FIELD).clear()
            self.driver.find_element(*AccountPageLocators.MOBILE_FIELD).send_keys(value)

    def clickOnRegister(self):
        self.driver.find_element(*AccountPageLocators.REGISTER_BTN).click()
        return MyPersonalAccount(self.driver)