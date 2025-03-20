from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class CheckoutCompletePage(GlobalPage):
    CONTINUE_SHOPPING_BUTTON = (By.NAME, "Continue Shopping button")