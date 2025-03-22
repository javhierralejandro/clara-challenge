import time

from behave import *
from selenium.common import StaleElementReferenceException, TimeoutException

from pages.catalog_page import CatalogPage
from utils.driver import get_driver

@given('the user navigates to the catalog page')
def step_go_to_catalog_page(context):
    context.driver = get_driver()
    context.catalog_page = CatalogPage(context.driver)

@when('the user clicks on the sort button')
def step_click_sort_button(context):
    context.catalog_page.click_sort_catalog()

@when('the user clicks on name ascending sort button')
def step_click_name_ascending_button(context):
    context.catalog_page.sort_name_ascending()


@when('the user clicks on name descending sort button')
def step_click_name_descending_button(context):
    context.catalog_page.sort_name_descending()


@when('the user clicks on price ascending sort button')
def step_click_price_ascending_button(context):
    context.catalog_page.sort_price_ascending()


@when('the user clicks on price descending sort button')
def step_click_price_descending_button(context):
    context.catalog_page.sort_price_descending()

@then('the user should see the catalog sorted by name ascending')
def step_verify_name_asc_sorted_catalog(context):
    context.catalog_page.verify_name_asc()

@then('the user should see the catalog sorted by name descending')
def step_verify_name_desc_sorted_catalog(context):
    context.catalog_page.verify_name_desc()

@then('the user should see the catalog sorted by price ascending')
def step_verify_price_asc_sorted_catalog(context):
    context.catalog_page.verify_price_asc()

@then('the user should see the catalog sorted by price descending')
def step_verify_price_asc_sorted_catalog(context):
    context.catalog_page.verify_price_desc()