from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class LoginPage(GlobalPage):
    USERNAME_TEXT_FIELD = (By.NAME, "Username input field")
    PASSWORD_TEXT_FIELD = (By.NAME, "Password input field")
    LOGIN_BUTTON= (By.NAME, "Login button")

    def enter_username(self, username):
        self.enter_text(self.USERNAME_TEXT_FIELD, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_TEXT_FIELD, password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)