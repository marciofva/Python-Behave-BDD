# Created by Marcio at 23/04/2017
Feature: Create a new account in the store
    Background: Access authentication page
      Given that I enter the URL "http://automationpractice.com/"
      And I click on "Sign In" button
      Then I should see the authentication page
      Given that I enter an email "Michael02@test.com"
      And I click on "Create an account" button
      Then I should see the account page

  Scenario: Fill the form out with valid data
      When I enter the values into the form
        |name                     |value        |
        |Title                    |Mr           |
        |Customer First Name      |Michael      |
        |Customer Last Name       |Conors       |
        |Password                 |1234adf      |
        |Day                      |15           |
        |Month                    |6            |
        |Year                     |1997         |
        |Newsletter               |yes          |
        |Special Offers           |yes          |
        |Address First Name       |Liam         |
        |Address Last Name        |Jackson      |
        |Company                  |IT Company   |
        |Address                  |Kent  st.    |
        |Country                  |United States|
        |City                     |Seattle      |
        |State                    |Massachusetts|
        |PostCode                 |12301        |
        |Mobile                   |0987300190   |
    And I click on "Register" button
    Then I should see the personal account page