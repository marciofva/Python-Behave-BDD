#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from behave import *

from common.Locators import LoginPageLocators, AccountPageLocators, MyPersonalAccountPage
from pageObjects.homePage import HomePage


@given('that I enter the URL "{url}"')
def step_impl(context,url):
    context.home = HomePage(context.driver)
    context.home.launchURL(url)

@step('I click on "{btn_name}" button')
def step_impl(context, btn_name):

    if 'Sign In' in btn_name:
        context.authentication = context.home.clickOnSignInBtn()
    elif 'Create an account' in btn_name:
        context.account = context.authentication.clickOnCreateAccountBtn()
    elif 'Register' in btn_name:
        context.myPersonalAccount = context.account.clickOnRegister()


@then("I should see the authentication page")
def step_impl(context):
    assert(context.home.elementIsPresent(*LoginPageLocators.CREATE_ACCOUNT_BTN) is True)


@given('that I enter an email "{email}"')
def step_impl(context, email):
    context.authentication.sendKeysSignUpEmail(email)


@then("I should see the account page")
def step_impl(context):
    assert (context.account.elementIsPresent(*AccountPageLocators.REGISTER_BTN) is True)


@then('I should see the following error message "{error_message}"')
def step_impl(context, error_message):
    assert (context.authentication.elementIsPresent(*AccountPageLocators.REGISTER_BTN) is False)
    assert (context.authentication.getErrorMessage() in error_message)


@when("I enter the values into the form")
def step_impl(context):
    for row in context.table:
        context.account.fillFormOut(row[0],row[1])


@then("I should see the personal account page")
def step_impl(context):
    assert (context.myPersonalAccount.elementIsPresent(*MyPersonalAccountPage.SIGNOUT_BTN) is True)