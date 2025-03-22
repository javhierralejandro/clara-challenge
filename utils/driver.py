from appium import webdriver
import yaml
from appium.options.android import UiAutomator2Options


def get_driver():
    # Load the configuration file
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Initialize UiAutomator2Options for Appium
    options = UiAutomator2Options()

    # Set capabilities for the Appium driver
    options.set_capability("platformName", config.get("platformName"))
    options.set_capability("deviceName", config.get("appium:deviceName"))
    options.set_capability("appPackage", config.get("appium:appPackage"))
    options.set_capability("appActivity", config.get("appium:appActivity"))
    options.set_capability("automationName", config.get("appium:automationName"))
    options.set_capability("noReset", config.get("appium:noReset"))
    options.set_capability("ensureWebviewsHavePages", config.get("appium:ensureWebviewsHavePages"))
    options.set_capability("disableWindowAnimation", config.get("appium:disableWindowAnimation"))
    options.set_capability("newCommandTimeout", config.get("appium:newCommandTimeout"))
    options.set_capability("app", config.get("appium:app"))

    # Create a new Appium driver instance with the specified options
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    return driver
