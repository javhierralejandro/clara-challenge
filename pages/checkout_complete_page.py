from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CheckoutCompletePage(GlobalPage):
    # Locators for various input fields and buttons on the checkout complete page
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='Continue Shopping button']")
    CHECKOUT_COMPLETE_TEXT = (By.XPATH, "//android.widget.TextView[@text='Checkout Complete']")

    # Method to validate that the checkout process is complete
    def validate_checkout_completion(self):
        # Find the checkout completion text element and get its text
        checkout_completion_text = self.find_element(self.CHECKOUT_COMPLETE_TEXT).text
        # Return the text of the checkout completion element
        return checkout_completion_text

    # Method to continue shopping after checkout is complete
    def continue_shopping(self):
        # Click the "Continue Shopping" button to continue shopping
        self.click_element(self.CONTINUE_SHOPPING_BUTTON)