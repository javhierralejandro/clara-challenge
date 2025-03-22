from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CheckoutPlaceOrderPage(GlobalPage):
    # Locator for button on the place order page
    PLACE_ORDER_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='Place Order button']")

    # Method to place an order
    def place_order(self):
        # Click the "Place Order" button to finalize the order
        self.click_element(self.PLACE_ORDER_BUTTON)