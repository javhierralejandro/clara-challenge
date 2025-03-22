from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver import get_driver

class GlobalPage:
    MENU_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='open menu']/android.widget.ImageView")
    CART_ITEM_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='cart badge']//android.widget.TextView")


    def __init__(self, driver=None):
        self.driver = driver or get_driver()
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
        # element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except:
            return False

    def get_cart_count(self):
        try:
            cart = self.find_element(self.CART_ITEM_BUTTON)
            return int(cart.text.strip())
        except:
            return 0

    def open_cart(self):
        self.click_element(self.CART_ITEM_BUTTON)

    def open_menu(self):
        self.click_element(self.MENU_BUTTON)
