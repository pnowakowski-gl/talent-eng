from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.config.config import config
from selenium.webdriver.remote.webelement import WebElement


class SignInPage:
    sign_in_button = (By.XPATH, '//a[contains(text(), "Sign in")]')
    sign_up_button = (By.XPATH, '//a[contains(text(), "Sign up")]')
    search_field = (By.XPATH, '//input[@aria-label="Search GitHub"]')

    def __init__(self, ui_app):
        self.ui_app = ui_app

    def go_to_page(self):
        self.ui_app.open_page(config.GITHUB_URL_UI)

    def go_to_sign_in_page(self):
        self.ui_app.click(*self.sign_in_button)

    def go_to_sign_up_page(self):
        self.ui_app.click(*self.sign_up_button)

    def search_github(self, text_to_search):
        self.ui_app.enter_text(*self.search_field, text_to_search)
        el = self.ui_app.get_element(*self.search_field)
        el.send_keys(Keys.RETURN)

    def sign_in_button_is_present(self):
        el = self.ui_app.get_element(*self.sign_in_button)
        return isinstance(el, WebElement)

    def github_search_is_working(self):
        self.search_github("testing search")
        el = self.ui_app.find_element(
            By.XPATH,
            '//div[@class="d-flex flex-column flex-md-row flex-justify-between border-bottom pb-3 position-relative"]/h3',
        )
        if "repository" in el.text:
            return True
        return False
