from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CatalogPage(GlobalPage):
    PRODUCTS = (By.ID, "A3030000-0000-0000-A814-000000000000")
