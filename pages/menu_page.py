from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class MenuPage(GlobalPage):
    # Locators for various elements on the menu page
    CATALOG_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='menu item catalog']")
    WEBVIEW_BUTTON = (By.XPATH,"//android.view.ViewGroup[@content-desc='menu item webview']code scanner")
    GEO_LOCATION_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='menu item qr code scanner']")
    DRAWING_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='menu item geo location']")
    REPORT_BUG_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='menu item drawing']")
    ABOUT_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='menu item about']")
    RESET_APP_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='menu item reset ap']")
    BIOMETRICS_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='menu item biometrics']")
    LOG_IN_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='menu item log in']")
    LOG_OUT_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='menu item log out']")
    API_CALLS_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='menu item log out']")
    SAUCE_BOT_VIDEO_BUTTON = (By.XPATH, "//android.view.ViewGroup[@content-desc='menu item log out']")

    # Method to click the login button
    def click_login(self):
        # Click the login button to log in
        self.click_element(self.LOG_IN_BUTTON)

    # Method to click the logout button
    def click_logout(self):
        # Click the logout button to log out
        self.click_element(self.LOG_OUT_BUTTON)

    # Method to open the catalog
    def open_catalog(self):
        # Click the catalog button to open the catalog
        self.click_element(self.CATALOG_BUTTON)