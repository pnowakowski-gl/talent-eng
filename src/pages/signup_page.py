from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.config.config import config


class SignupPage:
    sign_in_ = (By.XPATH, '//a[contains(text(), "Sign in")]')
    sign_up_ = (By.XPATH, '//a[contains(text(), "Sign up")]')
    search_ = (By.XPATH, '//input[@aria-label="Search GitHub"]')

    def __init__(self, ui_app):
        self.ui_app = ui_app

    def go_to_page(self):
        self.ui_app.open_page(config.GITHUB_URL_UI)

    def go_to_sign_in_page(self):
        self.ui_app.click(*self.sign_in_)

    def go_to_sign_up_page(self):
        self.ui_app.click(*self.sign_up_)

    def search_github(self, text_to_search):
        self.ui_app.enter_text(*self.search_, text_to_search)
        el = self.ui_app.get_element(*self.search_)
        el.send_keys(Keys.RETURN)
