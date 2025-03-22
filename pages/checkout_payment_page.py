from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CheckoutPaymentPage(GlobalPage):
    # Locators for various input fields and buttons on the checkout payment page
    CARD_FULL_NAME_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Full Name* input field']")
    CARD_NUMBER_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Card Number* input field']")
    EXPIRATION_DATE_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Expiration Date* input field']")
    SECURITY_CODE_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Security Code* input field']")
    BILLING_CHECK_BOX = (By.XPATH, "//android.view.ViewGroup[@content-desc='checkbox for My billing address is the same as my shipping address.']")
    REVIEW_ORDER_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='Review Order button']")
    # BILLING_FULLNAME_TEXT_FIELD = (By.XPATH,"(//android.widget.EditText[@content-desc='Full Name* input field'])[2]")
    # BILLING_ADDRESS_1_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Address Line 1* input field']")
    # BILLING_ADDRESS_2_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Address Line 2 input field']")
    # BILLING_CITY_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='City* input field']")
    # BILLING_STATE_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='State/Region input field']")
    # BILLING_ZIPCODE_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Zip Code* input field']")
    # BILLING_COUNTRY_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Country* input field']")

    # Method to enter the full name on the card in the corresponding text field
    def enter_card_full_name(self, full_name):
        # Enter the provided full name into the card full name text field
        self.enter_text(self.CARD_FULL_NAME_TEXT_FIELD, full_name)

    # Method to enter the card number in the corresponding text field
    def enter_card_number(self, card_number):
        # Enter the provided card number into the card number text field
        self.enter_text(self.CARD_NUMBER_TEXT_FIELD, card_number)

    # Method to enter the expiration date in the corresponding text field
    def enter_expiration_date(self, expiration_date):
        # Enter the provided expiration date into the expiration date text field
        self.enter_text(self.EXPIRATION_DATE_TEXT_FIELD, expiration_date)

    # Method to enter the security code in the corresponding text field
    def enter_security_code(self, security_code):
        # Enter the provided security code into the security code text field
        self.enter_text(self.SECURITY_CODE_TEXT_FIELD, security_code)

    # Method to verify if the billing address checkbox is selected
    def verify_checkbox(self):
        # Find the billing checkbox element and check if it is selected
        billing_checkbox = self.find_element(self.BILLING_CHECK_BOX)
        is_checked = billing_checkbox.is_selected()
        return is_checked

    # Method to click the review order button
    def review_order(self):
        # Click the review order button to proceed
        self.click_element(self.REVIEW_ORDER_BUTTON)

    # Method to enter billing information (commented out)
    # def enter_billing_info(self, fullname, address_1, address_2, city, state, zipcode, country):
    #    self.enter_text(self.BILLING_FULLNAME_TEXT_FIELD, fullname)
    #    self.enter_text(self.BILLING_ADDRESS_1_TEXT_FIELD, address_1)
    #    self.enter_text(self.BILLING_ADDRESS_2_TEXT_FIELD, address_2)
    #    self.enter_text(self.BILLING_CITY_TEXT_FIELD, city)
    #    self.enter_text(self.BILLING_STATE_TEXT_FIELD, state)
    #    self.enter_text(self.BILLING_ZIPCODE_TEXT_FIELD, zipcode)
    #    self.enter_text(self.BILLING_COUNTRY_FIELD, country)
