from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CheckoutAddressPage(GlobalPage):
    FULL_NAME_TEXT_FIELD = (By.NAME, "Full Name* input field")
    ADDRESS_1_TEXT_FIELD = (By.NAME, "Address Line 1* input field")
    ADDRESS_2_TEXT_FIELD = (By.NAME, "Address Line 2 Entrance 1")
    CITY_TEXT_FIELD = (By.NAME, "City* input field")
    STATE_TEXT_FIELD = (By.NAME, "State/Region input field")
    ZIPCODE_TEXT_FIELD = (By.NAME, "Zip Code* input field")
    COUNTRY_TEXT_FIELD = (By.NAME, "Country* input field")
    TO_PAYMENT_BUTTON = (By.NAME, "To Payment button")
    