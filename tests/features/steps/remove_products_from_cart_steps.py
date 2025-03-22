import time

from behave import *

from pages.cart_page import CartPage
from pages.global_page import GlobalPage
from utils.driver import get_driver

@given('the user has at least one product in the cart')
def step_validate_products_in_cart(context):
    context.driver = get_driver()
    context.global_page = GlobalPage(context.driver)
    initial_cart_count = context.global_page.get_cart_count()

    assert initial_cart_count > 0, f"Expected at least 1 product in the cart, but found {initial_cart_count}"

    context.global_page.open_cart()
    context.cart_page = CartPage(context.driver)

    context.initial_cart_count = initial_cart_count

@when('the user clicks on Remove Item')
def remove_product_from_cart(context):
    context.cart_page.remove_item()
    context.global_page = GlobalPage(context.driver)

@then('the product should be removed from cart')
def verify_product_removal_from_cart(context):
    time.sleep(1)
    final_cart_count = context.global_page.get_cart_count()

    assert final_cart_count == context.initial_cart_count - 1, "Error: the product was not removed correctly."