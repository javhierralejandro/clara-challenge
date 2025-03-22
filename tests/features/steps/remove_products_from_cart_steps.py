import time

from behave import *

from pages.cart_page import CartPage
from pages.global_page import GlobalPage
from utils.driver import get_driver

# Step definition for validating that the user has at least one product in the cart
@given('the user has at least one product in the cart')
def step_validate_products_in_cart(context):
    # Initialize the driver and global page
    context.driver = get_driver()
    context.global_page = GlobalPage(context.driver)

    # Get the current cart count
    initial_cart_count = context.global_page.get_cart_count()

    # Validate that the cart count is greater than 0
    assert initial_cart_count > 0, f"Expected at least 1 product in the cart, but found {initial_cart_count}"

    # Open the cart page
    context.global_page.open_cart()
    context.cart_page = CartPage(context.driver)

    # Store the initial cart count
    context.initial_cart_count = initial_cart_count

# Step definition for removing a product from the cart
@when('the user clicks on Remove Item')
def remove_product_from_cart(context):
    # Remove the product from the cart
    context.cart_page.remove_item()
    context.global_page = GlobalPage(context.driver)

# Step definition for verifying that the product was removed from the cart
@then('the product should be removed from cart')
def verify_product_removal_from_cart(context):
    time.sleep(1)
    # Get the final cart count
    final_cart_count = context.global_page.get_cart_count()

    # Validate that the final cart count is equal to the initial cart count minus 1
    assert final_cart_count == context.initial_cart_count - 1, "Error: the product was not removed correctly."