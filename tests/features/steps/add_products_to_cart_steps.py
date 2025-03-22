import time

from behave import *
from pages.catalog_page import CatalogPage
from pages.global_page import GlobalPage
from pages.product_page import ProductPage
from pages.menu_page import MenuPage
from utils.driver import get_driver

@given('the user is on the catalog page')
def step_go_to_catalog_page(context):
    context.driver = get_driver()
    context.catalog_page = CatalogPage(context.driver)

@when('the user selects product {index} in the catalog page')
def step_select_product_in_catalog(context, index):
    index = int(index)
    context.catalog_page.select_product(index)
    context.product_page = ProductPage(context.driver)

@when('the user adds product to cart')
def step_add_product_to_cart(context):
    context.product_page.add_product_to_cart()
    context.global_page = GlobalPage(context.driver)
    context.global_page.open_menu()
    context.menu_page = MenuPage(context.driver)
    context.menu_page.open_catalog()

@then('the cart should contain {num} product(s)')
def step_verify_cart_single_product(context, num):
    expected_cart_count = int(num)
    time.sleep(1)
    context.global_page = GlobalPage(context.driver)
    actual_cart_count = context.global_page.get_cart_count()

    assert actual_cart_count > 0, f"Expected {expected_cart_count} products, but found {actual_cart_count}"