import yaml
from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage


class ProductPage(GlobalPage):
    ADD_TO_CART_BUTTON = (By.NAME, "Add To Cart button")
    COUNTER_MINUS_BUTTON = (By.NAME, "counter minus button")
    COUNTER_PLUS_BUTTON = (By.NAME, "counter plus button")

    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    color_circle = config["color_circle"]
    COLOR_CIRCLE_BUTTON = (By.NAME, f"{color_circle} circle button")
    review_star = config["review_star"]
    REVIEW_STAR_BUTTON = (By.NAME, f"review star {review_star}")
    NAVIGATION_BACK_BUTTON = (By.NAME, "navigation back button")

    def launch_app(self):
        self.driver.launch_app()

    def add_product_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    def increase_item_amount(self):
        self.click_element(self.COUNTER_PLUS_BUTTON)

    def decrease_item_amount(self):
        self.click_element(self.COUNTER_MINUS_BUTTON)
