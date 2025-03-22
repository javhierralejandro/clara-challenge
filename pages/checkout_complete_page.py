from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CheckoutCompletePage(GlobalPage):
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='Continue Shopping button']")
    CHECKOUT_COMPLETE_TEXT = (By.XPATH, "//android.widget.TextView[@text='Checkout Complete']")

    def validate_checkout_completion(self):
        checkout_completion_text = self.find_element(self.CHECKOUT_COMPLETE_TEXT).text
        return checkout_completion_text

    def continue_shopping(self):
        self.click_element(self.CONTINUE_SHOPPING_BUTTON)