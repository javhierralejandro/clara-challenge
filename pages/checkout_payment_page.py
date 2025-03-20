from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CheckoutPaymentPage(GlobalPage):
    FULL_NAME_TEXT_FIELD = (By.NAME, "Full Name* input field")
    CARD_NUMBER_TEXT_FIELD = (By.NAME, "Card Number* input field")
    EXPIRATION_DATE_TEXT_FIELD = (By.NAME, "Expiration Date* input field")
    SECURITY_CODE = (By.NAME, "Security Code* input field")
    BILLING_CHECK_BOX = (By.NAME, "checkbox for My billing address is the same as my shipping address.")
    REVIEW_ORDER_BUTTON = (By.NAME, "Review Order button")
    BILLING_FULLNAME_TEXT_FIELD = (By.XPATH,"(//XCUIElementTypeTextField[@name='Full Name* input field'])[2]")
    BILLING_ADDRESS_1_TEXT_FIELD = (By.NAME, "Address Line 1* input field")
    BILLING_ADDRESS_2_TEXT_FIELD = (By.NAME, "Address Line 2 input field")
    BILLING_CITY_TEXT_FIELD = (By.NAME, "City* input field")
    BILLING_STATE_TEXT_FIELD = (By.NAME, "State/Region input field")
    BILLING_ZIPCODE_TEXT_FIELD = (By.NAME, "Zip Code* input field")
    BILLING_COUNTRY_FIELD = (By.NAME, "Country* input field")