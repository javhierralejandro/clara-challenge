from behave import *

from pages.catalog_page import CatalogPage
from utils.driver import get_driver

# Step definition for navigating to the catalog page
@given('the user navigates to the catalog page')
def step_go_to_catalog_page(context):
    # Initialize the driver and catalog page
    context.driver = get_driver()
    context.catalog_page = CatalogPage(context.driver)

# Step definition for clicking the sort button
@when('the user clicks on the sort button')
def step_click_sort_button(context):
    # Click the sort button on the catalog page
    context.catalog_page.click_sort_catalog()

# Step definition for sorting by name in ascending order
@when('the user clicks on name ascending sort button')
def step_click_name_ascending_button(context):
    # Click the name ascending sort button
    context.catalog_page.sort_name_ascending()

# Step definition for sorting by name in descending order
@when('the user clicks on name descending sort button')
def step_click_name_descending_button(context):
    # Click the name descending sort button
    context.catalog_page.sort_name_descending()

# Step definition for sorting by price in ascending order
@when('the user clicks on price ascending sort button')
def step_click_price_ascending_button(context):
    # Click the price ascending sort button
    context.catalog_page.sort_price_ascending()

# Step definition for sorting by price in descending order
@when('the user clicks on price descending sort button')
def step_click_price_descending_button(context):
    # Click the price descending sort button
    context.catalog_page.sort_price_descending()

# Step definition for verifying the catalog is sorted by name in ascending order
@then('the user should see the catalog sorted by name ascending')
def step_verify_name_asc_sorted_catalog(context):
    # Verify the catalog is sorted by name ascending
    context.catalog_page.verify_name_asc()

# Step definition for verifying the catalog is sorted by name in descending order
@then('the user should see the catalog sorted by name descending')
def step_verify_name_desc_sorted_catalog(context):
    # Verify the catalog is sorted by name descending
    context.catalog_page.verify_name_desc()

# Step definition for verifying the catalog is sorted by price in ascending order
@then('the user should see the catalog sorted by price ascending')
def step_verify_price_asc_sorted_catalog(context):
    context.catalog_page.verify_price_asc()

# Step definition for verifying the catalog is sorted by price in descending order
@then('the user should see the catalog sorted by price descending')
def step_verify_price_asc_sorted_catalog(context):
    # Verify the catalog is sorted by price descending
    context.catalog_page.verify_price_desc()