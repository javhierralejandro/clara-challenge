from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GlobalPage:
    CATALOG_BUTTON = (By.NAME, "tab bar option catalog")
    CART_BUTTON = (By.NAME, "tab bar option cart")
    MENU_BUTTON = (By.NAME, "tab bar option menu")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def open_catalog(self):
        self.click_element(self.CATALOG_BUTTON)

    def open_cart(self):
        self.click_element(self.CART_BUTTON)

    def open_menu(self):
        self.click_element(self.MENU_BUTTON)