from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CheckoutPlaceOrderPage(GlobalPage):
    PLACE_ORDER_BUTTON = (By.NAME, "Place Order button")