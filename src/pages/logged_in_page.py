from selenium.webdriver.common.by import By

from src.config.config import config


class LoggedInPage:
    logged_in_avatar = (By.XPATH, '//summary[@aria-label="View profile and more"]')
    sign_out = (By.XPATH, '//button[@data-ga-click="Header, sign out, icon:logout"]')

    def __init__(self, ui_app):
        self.ui_app = ui_app

    def log_out(self):
        self.ui_app.wait_for_element_to_be_present(*self.logged_in_avatar)
        self.ui_app.click(*self.logged_in_avatar)
        self.ui_app.wait_for_element_to_be_present(*self.sign_out)
        self.ui_app.click(*self.sign_out)
