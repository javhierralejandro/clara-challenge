from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CheckoutAddressPage(GlobalPage):
    FULL_NAME_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Full Name* input field']")
    ADDRESS_1_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Address Line 1* input field']")
    ADDRESS_2_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Address Line 2 input field']")
    CITY_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='City* input field']")
    STATE_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='State/Region input field']")
    ZIPCODE_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Zip Code* input field']")
    COUNTRY_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Country* input field']")
    TO_PAYMENT_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='To Payment button']")

    def enter_full_name(self, full_name):
        self.enter_text(self.FULL_NAME_TEXT_FIELD, full_name)

    def enter_address_1(self, address_1):
        self.enter_text(self.ADDRESS_1_TEXT_FIELD, address_1)

    def enter_address_2(self, address_2):
        self.enter_text(self.ADDRESS_2_TEXT_FIELD, address_2)

    def enter_city(self, city):
        self.enter_text(self.CITY_TEXT_FIELD, city)

    def enter_state(self, state):
        self.enter_text(self.STATE_TEXT_FIELD, state)

    def enter_zipcode(self, zipcode):
        self.enter_text(self.ZIPCODE_TEXT_FIELD, zipcode)

    def enter_country(self, country):
        self.enter_text(self.COUNTRY_TEXT_FIELD, country)

    def proceed_to_payment(self):
        self.click_element(self.TO_PAYMENT_BUTTON)