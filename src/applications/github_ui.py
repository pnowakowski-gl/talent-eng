import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from src.applications.base_app_ui import BaseUIApp
from src.config.config import config


class GitHubUI(BaseUIApp):
    """
    Use abstract methods to perform action on GitHub page.
    """

    def __init__(self, browser) -> None:
        super().__init__(browser)

    def open_base_page(self) -> None:
        self.open_page(config.GITHUB_URL_UI)

    def goto_login_page(self) -> None:
        self.wait_for_element_to_be_present(By.LINK_TEXT, "Sign in")
        self.click(By.LINK_TEXT, "Sign in")

    def login_to_page(self, username: str, password: str) -> None:
        self.wait_for_element_to_be_present(By.ID, "login_field")
        self.enter_text(By.ID, "login_field", username)
        self.enter_text(By.ID, "password", password)
        self.click(By.NAME, "commit")

    def logout_off_page(self) -> None:
        """
        Logs off page by finding elements that are present if you are logged in.
        """
        self.wait_for_element_to_be_present(
            By.XPATH, '//summary[@aria-label="View profile and more"]'
        )
        self.click(By.XPATH, '//summary[@aria-label="View profile and more"]')
        self.wait_for_element_to_be_present(
            By.XPATH,
            '//button[@data-ga-click="Header, sign out, icon:logout"]',
        )
        self.click(
            By.XPATH,
            '//button[@data-ga-click="Header, sign out, icon:logout"]',
        )

    def find_text(self, locator_type: By, locator_name: str) -> str:
        """
        Returns text found with given locator type and name.
        """
        self.wait_for_element_to_be_present(locator_type, locator_name)
        return self.get_element(locator_type, locator_name).text

    def close_current_browser(self):
        self.close_browser()
