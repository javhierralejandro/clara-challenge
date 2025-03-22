# Clara Challenge

Practical Task for Clara's QA Engineer position. Automation Framework to test a Shopping App from Saucelabs.

## Description

This project is an automation framework built using Appium, Python, and Behave to test various functionalities of a shopping app. The following functionalities are automated:
1. Add a product to the cart
2. Filters
3. Checkout
4. Drag and drop (OPTIONAL)

## Installation

To install the dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Configuration

Ensure that the Appium server is running and you have an Android device or emulator started. iOS is not supported yet. The capabilities are defined in the config.yaml file.

## Running the tests

To run the tests, execute the following command:

```bash
behave tests/features/<feature_name>.feature -f pretty -o reports/resultado.html
```

## Reports

The reports are generated in the reports/ folder. The reports are generated in HTML format. For example, to run the add_products_to_cart.feature test and generate an HTML report, use:

```bash
behave tests/features/add_products_to_cart.feature -f pretty -o reports/resultado.html
```

## Example Usage

Here is an example of how to use the framework to validate that the user has at least one product in the cart:

```python
@given('the user has at least one product in cart')
def step_validate_products_in_cart(context):
    context.driver = get_driver()
    context.global_page = GlobalPage(context.driver)
    actual_cart_count = context.global_page.get_cart_count()
    assert actual_cart_count > 0, f"Expected at least 1 product in the cart, but found {actual_cart_count}"
    context.global_page.open_cart()
    context.cart_page = CartPage(context.driver)
```

## Author

Javier Alejandro Espinoza Castillo