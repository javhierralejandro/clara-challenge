from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CartPage(GlobalPage):
    GO_SHOPPING_BUTTON = (By.NAME, "Go Shopping button")
    REMOVE_ITEM_BUTTON = (By.NAME, "remove item")
    COUNTER_MINUS_BUTTON = (By.NAME, "counter minus button")
    COUNTER_PLUS_BUTTON = (By.NAME, "counter plus button")
    CHECKOUT_BUTTON =  (By.NAME, "Proceed To Checkout button")
    