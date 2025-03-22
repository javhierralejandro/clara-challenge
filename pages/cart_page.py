from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CartPage(GlobalPage):
    REMOVE_ITEM_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='remove item']")
    COUNTER_MINUS_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='counter minus button']")
    COUNTER_PLUS_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='counter plus button']")
    CHECKOUT_BUTTON =  (By.XPATH, "//android.view.ViewGroup[@content-desc='Proceed To Checkout button']")

    def count_products(self):
        try:
            products = self.find_elements(self.REMOVE_ITEM_BUTTON)
            products_quantity = len(products)
            return products_quantity
        except Exception as e:
            print(f"There is a problem retrieving the number of products: {e}")

    def remove_item(self):
        products_quantity = self.count_products()
        if products_quantity > 1:
            product_xpath = "(" + self.REMOVE_ITEM_BUTTON[1] + f")[{products_quantity}]"
            product_element_locator = (By.XPATH, product_xpath)
            self.click_element(product_element_locator)
        else:
            self.click_element(self.REMOVE_ITEM_BUTTON)

    def proceed_to_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)