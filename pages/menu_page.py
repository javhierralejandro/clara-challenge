from selenium.webdriver.common.by import By

from pages.global_page import GlobalPage

class MenuPage(GlobalPage):
    WEBVIEW_BUTTON = (By.NAME,"menu item webview")
    QR_SCANNER_BUTTON = (By.NAME, "menu item qr code scanner")
    GEO_LOCATION_BUTTON = (By.NAME, "menu item geo location")
    DRAWING_BUTTON = (By.NAME, "menu item drawing")
    REPORT_BUG_BUTTON = (By.NAME, "menu item report a bug")
    ABOUT_BUTTON = (By.NAME, "menu item about")
    RESET_APP_BUTTON = (By.NAME, "menu item reset app")
    FACE_ID_BUTTON = (By.NAME, "FaceID")
    LOG_IN_BUTTON = (By.NAME, "menu item log in")
    LOG_OUT_BUTTON = (By.NAME, "menu item log out")
    API_CALLS_BUTTON = (By.NAME, "menu item api calls")
    SAUCE_BOT_VIDEO_BUTTON = (By.NAME, "menu item sauce bot video")
