from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CheckoutAddressPage(GlobalPage):
    # Locators for various input fields and buttons on the checkout address page
    FULL_NAME_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Full Name* input field']")
    ADDRESS_1_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Address Line 1* input field']")
    ADDRESS_2_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Address Line 2 input field']")
    CITY_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='City* input field']")
    STATE_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='State/Region input field']")
    ZIPCODE_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Zip Code* input field']")
    COUNTRY_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Country* input field']")
    TO_PAYMENT_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='To Payment button']")

    # Method to enter the full name in the corresponding text field
    def enter_full_name(self, full_name):
        # Enter the provided full name into the full name text field
        self.enter_text(self.FULL_NAME_TEXT_FIELD, full_name)

    # Method to enter the address line 1 in the corresponding text field
    def enter_address_1(self, address_1):
        # Enter the provided address line 1 into the address line 1 text field
        self.enter_text(self.ADDRESS_1_TEXT_FIELD, address_1)

    # Method to enter the address line 2 in the corresponding text field
    def enter_address_2(self, address_2):
        # Enter the provided address line 2 into the address line 2 text field
        self.enter_text(self.ADDRESS_2_TEXT_FIELD, address_2)

    # Method to enter the city in the corresponding text field
    def enter_city(self, city):
        # Enter the provided city into the city text field
        self.enter_text(self.CITY_TEXT_FIELD, city)

    # Method to enter the state in the corresponding text field
    def enter_state(self, state):
        # Enter the provided state into the state text field
        self.enter_text(self.STATE_TEXT_FIELD, state)

    # Method to enter the zip code in the corresponding text field
    def enter_zipcode(self, zipcode):
        # Enter the provided zip code into the zip code text field
        self.enter_text(self.ZIPCODE_TEXT_FIELD, zipcode)

    # Method to enter the country in the corresponding text field
    def enter_country(self, country):
        # Enter the provided country into the country text field
        self.enter_text(self.COUNTRY_TEXT_FIELD, country)

    # Method to proceed to the payment page
    def proceed_to_payment(self):
        # Click the button to proceed to the payment page
        self.click_element(self.TO_PAYMENT_BUTTON)