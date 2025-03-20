from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CatalogPage(GlobalPage):
    PRODUCTS_ELEMENT = (By.ID, "08000000-0000-0000-A814-000000000000")
    SORT_BUTTON = (By.NAME, "sort button")
    NAME_ASCENDING_SORT_BUTTON = (By.NAME, "Name - Ascending")
    NAME_DESCENDING_SORT_BUTTON = (By.NAME, "Name - Descending")
    PRICE_ASCENDING_SORT_BUTTON = (By.NAME, "priceAsc")
    PRICE_DESCENDING_SORT_BUTTON = (By.NAME, "Price - Descending")

    def get_products(self):
        try:
            products = self.find_elements(self.PRODUCTS_ELEMENT)
            products_list = []
            for product_element in products:
                products_list.append(product_element)
            return products_list
        except Exception as e:
            print(f"There is a problem retrieving the products: {e}")

    def select_product(self, product_number):
        products = self.get_products()
        self.click_element(products[product_number])

    def click_sort_catalog(self):
        self.click_element(self.SORT_BUTTON)

    def sort_name_ascending(self):
        self.click_sort_catalog()
        self.click_element(self.NAME_ASCENDING_SORT_BUTTON)

    def sort_name_descending(self):
        self.click_sort_catalog()
        self.click_element(self.NAME_DESCENDING_SORT_BUTTON)

    def sort_price_ascending(self):
        self.click_sort_catalog()
        self.click_element(self.PRICE_ASCENDING_SORT_BUTTON)

    def sort_price_descending(self):
        self.click_sort_catalog()
        self.click_element(self.PRICE_DESCENDING_SORT_BUTTON)