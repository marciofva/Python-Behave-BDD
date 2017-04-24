from selenium.webdriver.common.by import By

class HomePageLocators(object):
    SIGNIN_BTN = (By.CLASS_NAME, 'login')
    CONTACT_BTN = (By.ID, 'contact-link')

class LoginPageLocators(object):
    EMAIL_FIELD = (By.ID, 'email_create')
    CREATE_ACCOUNT_BTN = (By.ID, 'SubmitCreate')
    EMAIL_ERROR = (By.ID, 'create_account_error')

class AccountPageLocators(object):
    TITLE_MR_RADIO = (By.ID, 'id_gender1')
    TITLE_MRS_RADIO = (By.ID, 'id_gender1')
    CUSTOMER_FIRST_NAME_FIELD = (By.ID, 'customer_firstname')
    CUSTOMER_LAST_NAME_FIELD = (By.ID, 'customer_lastname')
    PASSWORD_FIELD = (By.ID, 'passwd')
    DAY_DROPDOWN = (By.ID, 'days')
    MONTH_DROPDOWN = (By.ID, 'months')
    YEAR_DROPDOWN = (By.ID, 'years')
    NEWSLETTER_CHECKBOX = (By.ID, 'newsletter')
    OPTION_CHECKBOX = (By.ID, 'optin')
    FIRST_NAME_FIELD = (By.ID, 'firstname')
    LAST_NAME_FIELD = (By.ID, 'lastname')
    COMPANY_FIELD = (By.ID, 'company')
    ADDRESS_FIELD = (By.ID, 'address1')
    CITY_FIELD = (By.ID, 'city')
    STATE_DROPDOWN = (By.ID, 'id_state')
    POSTCODE_FIELD = (By.ID, 'postcode')
    COUNTRY_DROPDOWN = (By.ID, 'id_country')
    MOBILE_FIELD = (By.ID, 'phone_mobile')
    REGISTER_BTN = (By.ID, 'submitAccount')

class MyPersonalAccountPage(object):
    SIGNOUT_BTN = (By.CLASS_NAME, 'logout')




