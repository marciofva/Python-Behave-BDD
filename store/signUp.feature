# Created by Marcio at 23/04/2017
Feature: SignUp in the store

  Background: Access authentication page
    Given that I enter the URL "http://automationpractice.com/"
    And I click on "Sign In" button
    Then I should see the authentication page

  Scenario: Enter a valid email
    Given that I enter an email "jhon@test.com"
    And I click on "Create an account" button
    Then I should see the account page

  Scenario: Enter an invalid email
    Given that I enter an email "mary@@"
    And I click on "Create an account" button
    Then I should see the following error message "Invalid email address."
