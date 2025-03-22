from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class LoginPage(GlobalPage):
    # Locators for the elements on the login page
    USERNAME_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Username input field']")
    PASSWORD_TEXT_FIELD = (By.XPATH, "//android.widget.EditText[@content-desc='Password input field']")
    LOGIN_BUTTON= (By.XPATH, "//android.view.ViewGroup[@content-desc='Login button']")

    # Method to enter the username in the corresponding text field
    def enter_username(self, username):
        # Enter the provided username into the username text field
        self.enter_text(self.USERNAME_TEXT_FIELD, username)

    # Method to enter the password in the corresponding text field
    def enter_password(self, password):
        # Enter the provided password into the password text field
        self.enter_text(self.PASSWORD_TEXT_FIELD, password)

    # Method to click the login button
    def click_login(self):
        # Click the login button to attempt login
        self.click_element(self.LOGIN_BUTTON)