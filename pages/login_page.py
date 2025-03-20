from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class LoginPage(GlobalPage):
    USERNAME_TEXT_FIELD = (By.NAME, "Username input field")
    PASSWORD_TEXT_FIELD = (By.NAME, "Password input field")
    LOGIN_BUTTON= (By.NAME, "Login button")