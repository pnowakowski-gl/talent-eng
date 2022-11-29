from selenium.webdriver.common.by import By

from src.config.config import config
from selenium.webdriver.remote.webelement import WebElement


class PnowakowskiLoggedIn:
    logged_in_avatar = (By.XPATH, '//summary[@aria-label="View profile and more"]')
    sign_out = (By.XPATH, '//button[@data-ga-click="Header, sign out, icon:logout"]')

    def __init__(self, ui_app):
        self.ui_app = ui_app

    def user_logged_in(self) -> bool:
        """
        Checks if user is logged in and returns True if it is.
        """
        el = self.ui_app.get_element(*self.logged_in_avatar)
        return isinstance(el, WebElement)

    def log_out(self) -> None:
        """
        Logs out the user.
        """
        self.ui_app.click(*self.logged_in_avatar)
        self.ui_app.click(*self.sign_out)
