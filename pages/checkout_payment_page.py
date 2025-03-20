from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CheckoutPaymentPage(GlobalPage):
    FULL_NAME_TEXT_FIELD = (By.NAME, "Full Name* input field")
    CARD_NUMBER_TEXT_FIELD = (By.NAME, "Card Number* input field")
    EXPIRATION_DATE_TEXT_FIELD = (By.NAME, "Expiration Date* input field")
    SECURITY_CODE_TEXT_FIELD = (By.NAME, "Security Code* input field")
    BILLING_CHECK_BOX = (By.NAME, "checkbox for My billing address is the same as my shipping address.")
    REVIEW_ORDER_BUTTON = (By.NAME, "Review Order button")
    BILLING_FULLNAME_TEXT_FIELD = (By.XPATH,"(//XCUIElementTypeTextField[@name='Full Name* input field'])[2]")
    BILLING_ADDRESS_1_TEXT_FIELD = (By.NAME, "Address Line 1* input field")
    BILLING_ADDRESS_2_TEXT_FIELD = (By.NAME, "Address Line 2 input field")
    BILLING_CITY_TEXT_FIELD = (By.NAME, "City* input field")
    BILLING_STATE_TEXT_FIELD = (By.NAME, "State/Region input field")
    BILLING_ZIPCODE_TEXT_FIELD = (By.NAME, "Zip Code* input field")
    BILLING_COUNTRY_FIELD = (By.NAME, "Country* input field")

    def enter_full_name(self, full_name):
        self.enter_text(self.FULL_NAME_TEXT_FIELD, full_name)

    def enter_card_number(self, card_number):
        self.enter_text(self.CARD_NUMBER_TEXT_FIELD, card_number)

    def enter_expiration_date(self, expiration_date):
        self.enter_text(self.EXPIRATION_DATE_TEXT_FIELD, expiration_date)

    def enter_security_code(self, security_code):
        self.enter_text(self.SECURITY_CODE_TEXT_FIELD, security_code)

    def verify_checkbox(self):
        billing_checkbox = self.find_element(self.BILLING_CHECK_BOX)
        is_checked = billing_checkbox.is_selected()
        return is_checked

    def review_order(self, fullname, address_1, address_2, city, state, zipcode, country):
        billing_checkbox = self.verify_checkbox()
        if billing_checkbox:
            self.click_element(self.REVIEW_ORDER_BUTTON)
        else:
            self.enter_text(self.BILLING_FULLNAME_TEXT_FIELD, fullname)
            self.enter_text(self.BILLING_ADDRESS_1_TEXT_FIELD, address_1)
            self.enter_text(self.BILLING_ADDRESS_2_TEXT_FIELD, address_2)
            self.enter_text(self.BILLING_CITY_TEXT_FIELD, city)
            self.enter_text(self.BILLING_STATE_TEXT_FIELD, state)
            self.enter_text(self.BILLING_ZIPCODE_TEXT_FIELD, zipcode)
            self.enter_text(self.BILLING_COUNTRY_FIELD, country)
            self.click_element(self.REVIEW_ORDER_BUTTON)