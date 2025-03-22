from selenium.webdriver.common.by import By
from pages.global_page import GlobalPage

class CatalogPage(GlobalPage):
    # Locators for various elements on the catalog page
    SORT_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='sort button']")
    PRODUCT_ELEMENT = (By.XPATH, "(//android.view.ViewGroup[@content-desc='products screen']//android.view.ViewGroup[@content-desc='store item'])[{}]")
    PRODUCT_PRICE_ELEMENT = (By.XPATH, "(//android.view.ViewGroup[@content-desc='store item'])[{}]//android.widget.TextView[@content-desc='store item price']")
    NAME_ASCENDING_SORT_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='nameAsc']")
    NAME_DESCENDING_SORT_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='nameDesc']")
    PRICE_ASCENDING_SORT_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='priceAsc']")
    PRICE_DESCENDING_SORT_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='priceDesc']")

    # Method to select a product by its index number
    def select_product(self, product_number):
        # Construct the XPath for the product and click it
        product_xpath = self.PRODUCT_ELEMENT[1].format(product_number)
        product_element_locator = (By.XPATH, product_xpath)
        self.click_element(product_element_locator)

    # Method to click the sort button on the catalog page
    def click_sort_catalog(self):
        self.click_element(self.SORT_BUTTON)

    # Method to sort products by name in ascending order
    def sort_name_ascending(self):
        self.click_element(self.NAME_ASCENDING_SORT_BUTTON)

    # Method to sort products by name in descending order
    def sort_name_descending(self):
        self.click_element(self.NAME_DESCENDING_SORT_BUTTON)

    # Method to sort products by price in ascending order
    def sort_price_ascending(self):
        self.click_element(self.PRICE_ASCENDING_SORT_BUTTON)

    # Method to sort products by price in descending order
    def sort_price_descending(self):
        self.click_element(self.PRICE_DESCENDING_SORT_BUTTON)

    # Method to verify that products are sorted by name in ascending order
    def verify_name_asc(self):
        products_names = []
        for i in range(1,7):
            # Construct the XPath for each product and get its name
            product_xpath = self.PRODUCT_ELEMENT[1].format(i)
            product_element_locator = (By.XPATH, product_xpath)
            product_element = self.find_element(product_element_locator)
            product_name = product_element.get_attribute("content-desc")
            products_names.append(product_name)

        # Assert that the product names are sorted in ascending order
        assert products_names == sorted(products_names), f"Error: the catalog is not correctly sorted. List: {products_names}"

    # Method to verify that products are sorted by name in descending order
    def verify_name_desc(self):
        products_names = []
        for i in range(1,7):
            # Construct the XPath for each product and get its name
            product_xpath = self.PRODUCT_ELEMENT[1].format(i)
            product_element_locator = (By.XPATH, product_xpath)
            product_element = self.find_element(product_element_locator)
            product_name = product_element.get_attribute("content-desc")
            products_names.append(product_name)

        # Assert that the product names are sorted in descending order
        assert products_names == sorted(products_names, reverse=True), f"Error: the catalog is not correctly sorted. List: {products_names}"

    # Method to verify that products are sorted by price in ascending order
    def verify_price_asc(self):
        products_prices = []
        for i in range(1,7):
            # Construct the XPath for each product and get its price
            product_xpath = self.PRODUCT_PRICE_ELEMENT[1].format(i)
            product_element_locator = (By.XPATH, product_xpath)
            product_element = self.find_element(product_element_locator)
            product_price_text = product_element.text.replace("$","").replace(",","").strip()
            products_prices.append(float(product_price_text))

        # Assert that the product prices are sorted in ascending order
        assert products_prices == sorted(products_prices), f"Error: the catalog is not correctly sorted. List: {products_prices}"

    # Method to verify that products are sorted by price in descending order
    def verify_price_desc(self):
        products_prices = []
        for i in range(1,7):
            # Construct the XPath for each product and get its price
            product_xpath = self.PRODUCT_PRICE_ELEMENT[1].format(i)
            print(product_xpath)
            product_element_locator = (By.XPATH, product_xpath)
            product_element = self.find_element(product_element_locator)
            product_price_text = product_element.text.replace("$", "").strip()
            products_prices.append(float(product_price_text))

        # Assert that the product prices are sorted in descending order
        assert products_prices == sorted(products_prices, reverse=True), f"Error: the catalog is not correctly sorted. List: {products_prices}"