from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CartPage(GlobalPage):
    REMOVE_ITEM_BUTTON = (By.NAME, "remove item")
    COUNTER_MINUS_BUTTON = (By.NAME, "counter minus button")
    COUNTER_PLUS_BUTTON = (By.NAME, "counter plus button")
    CHECKOUT_BUTTON =  (By.NAME, "Proceed To Checkout button")

    def count_products(self):
        try:
            products = self.find_elements(self.REMOVE_ITEM_BUTTON)
            products_quantity = len(products)
            return products_quantity
        except Exception as e:
            print(f"There is a problem retrieving the number of products: {e}")


    def remove_item(self, number):
        products_quantity = self.count_products()
        if products_quantity > 1:
            self.click_element((By.XPATH, f"(//XCUIElementTypeOther[@name='remove item'])[{number}]"))
        else:
            self.click_element(self.REMOVE_ITEM_BUTTON)

    def proceed_to_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)