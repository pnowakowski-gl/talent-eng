import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from src.applications.baseAppUI import BaseUIApp
from src.config.config import config


class GitHubUI(BaseUIApp):
    """
    Use abstract methods to perform action on GitHub page.
    """

    def __init__(self) -> None:
        super().__init__()

    def open_base_page(self) -> None:
        self.open_page(config.GITHUB_URL_UI)

    def goto_login_page(self) -> None:
        self.click(By.LINK_TEXT, "Sign in")

    def login_to_page(self, username: str, password: str) -> None:
        self.enter_text(By.ID, "login_field", username)
        self.enter_text(By.ID, "password", password)
        self.click(By.NAME, "commit")

    def logout_off_page(self) -> None:
        """
        Tries to find logout button. If it's not found it means you are not logged in so it prints appropriate message.
        """
        try:
            self.click(
                By.XPATH, "/html/body/div[1]/header/div[7]/details/summary/span[2]"
            )
            time.sleep(2)
            self.click(
                By.XPATH,
                "/html/body/div[1]/header/div[7]/details/details-menu/form/button",
            )
        except NoSuchElementException:
            print("You are not logged in.")

    def check_if_text_is_present(self, locator_type: By, locator_name: str) -> str:
        return self.get_element(locator_type, locator_name).text
