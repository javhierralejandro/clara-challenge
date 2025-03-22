import time

from behave import *
from selenium.common import StaleElementReferenceException

from pages.global_page import GlobalPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.checkout_address_page import CheckoutAddressPage
from pages.checkout_payment_page import CheckoutPaymentPage
from pages.checkout_place_order_page import CheckoutPlaceOrderPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.menu_page import MenuPage
from utils.driver import get_driver

# Step definition for validating that the user has at least one product in the cart
@given('the user has at least one product in cart')
def step_validate_products_in_cart(context):
    # Initialize the driver and global page
    context.driver = get_driver()
    context.global_page = GlobalPage(context.driver)

    # Get the current cart count
    actual_cart_count = context.global_page.get_cart_count()

    # Validate that the cart count is greater than 0
    assert actual_cart_count > 0, f"Expected at least 1 product in the cart, but found {actual_cart_count}"

    # Open the cart page
    context.global_page.open_cart()
    context.cart_page = CartPage(context.driver)

# Step definition for proceeding to checkout
@when('the user proceeds to checkout')
def step_proceed_to_checkout(context):
    # Proceed to checkout from the cart page
    context.cart_page.proceed_to_checkout()
    context.login_page = LoginPage(context.driver)

# Step definition for logging in to proceed to checkout
@when('the user login to proceed to checkout')
def step_user_login(context):
    # Enter login credentials
    context.login_page.enter_username("bob@example.com")
    context.login_page.enter_password("10203040")

    # Click login button
    context.login_page.click_login()
    context.checkout_address_page = CheckoutAddressPage(context.driver)

# Step definition for entering shipping address
@when('the user enters a shipping address')
def step_shipping_address_registration(context):

    # Enter shipping address details
    context.checkout_address_page.enter_full_name("Rebecca Winter")
    context.checkout_address_page.enter_address_1("Mandorley 112")
    context.checkout_address_page.enter_address_2("Entrance 1")
    context.checkout_address_page.enter_city("Truro")
    context.checkout_address_page.enter_state("Cornwall")
    context.checkout_address_page.enter_zipcode("89750")
    context.checkout_address_page.enter_country("United Kingdom")

    # Proceed to payment page
    context.checkout_address_page.proceed_to_payment()
    context.checkout_payment_page = CheckoutPaymentPage(context.driver)

# Step definition for entering payment method
@when('the user enters a payment method')
def step_payment_method_registration(context):

    # Enter payment method details
    try:
        context.checkout_payment_page.enter_card_full_name("Rebecca Winter")
    except StaleElementReferenceException:
        context.checkout_payment_page.enter_card_full_name("Rebecca Winter")

    context.checkout_payment_page.enter_card_number("325812657568789")
    context.checkout_payment_page.enter_expiration_date("03/25")
    context.checkout_payment_page.enter_security_code("123")

    # Verify if billing address checkbox is checked
    billing_address_checkbox = context.checkout_payment_page.verify_checkbox()

    try:
        # If billing address checkbox is checked, proceed to review order
        assert billing_address_checkbox, "If is not checked, proceed to fill billing information"
        context.checkout_payment_page.review_order()

    except AssertionError:
        # If billing address checkbox is not checked, proceed to fill billing information
        # Note: During inspection with appium inspector, the billing address checkbox "is_selected" attribute is always false
        # context.checkout_payment_page.enter_billing_info("John Doe", "Evergreen terrace 742", "Entrance", "Springfield", "Unknown", "00000", "United States")
        context.checkout_payment_page.review_order()

    context.checkout_place_order_page = CheckoutPlaceOrderPage(context.driver)

# Step definition for placing the order
@when('the user places the order')
def step_placing_order(context):
    # Place the order
    context.checkout_place_order_page.place_order()
    context.checkout_complete_page = CheckoutCompletePage(context.driver)

# Step definition for verifying that the checkout is completed
@then('the products checkout should be completed')
def step_verify_checkout_completion(context):
    # Validate that the checkout is completed
    checkout_completion_text = context.checkout_complete_page.validate_checkout_completion()
    assert checkout_completion_text == "Checkout Complete", "Checkout completion failed"

    # Continue shopping
    context.checkout_complete_page.continue_shopping()

    # Step definition for logging out
    time.sleep(1)
    context.global_page = GlobalPage(context.driver)
    context.global_page.open_menu()
    context.menu_page = MenuPage(context.driver)
    context.menu_page.click_logout()

    # Handle the logout request alert
    logout_request_alert = context.driver.switch_to.alert
    logout_request_alert.accept()

    # Terminate the app
    time.sleep(1)
    context.driver.terminate_app("com.saucelabs.mydemoapp.rn")