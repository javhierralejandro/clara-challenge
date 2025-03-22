from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CartPage(GlobalPage):
    # Locators for various elements on the cart page
    REMOVE_ITEM_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='remove item']")
    COUNTER_MINUS_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='counter minus button']")
    COUNTER_PLUS_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='counter plus button']")
    CHECKOUT_BUTTON =  (By.XPATH, "//android.view.ViewGroup[@content-desc='Proceed To Checkout button']")

    # Method to count the number of products in the cart
    def count_products(self):
        try:
            # Find all elements matching the remove item button locator
            products = self.find_elements(self.REMOVE_ITEM_BUTTON)
            # Return the number of products found
            products_quantity = len(products)
            return products_quantity
        except Exception as e:
            print(f"There is a problem retrieving the number of products: {e}")

    # Method to remove an item from the cart
    def remove_item(self):
        # Get the current number of products in the cart
        products_quantity = self.count_products()
        if products_quantity > 1:
            # If more than one product, construct the XPath for the last product and click it
            product_xpath = "(" + self.REMOVE_ITEM_BUTTON[1] + f")[{products_quantity}]"
            product_element_locator = (By.XPATH, product_xpath)
            self.click_element(product_element_locator)
        else:
            # If only one product, click the remove item button directly
            self.click_element(self.REMOVE_ITEM_BUTTON)

    # Method to proceed to the checkout page
    def proceed_to_checkout(self):
        # Click the proceed to checkout button
        self.click_element(self.CHECKOUT_BUTTON)