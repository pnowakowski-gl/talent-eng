from selenium.webdriver.common.by import By

from src.applications.base_app_ui import BaseUIApp
from src.pages.forgot_password_page import ForgotPasswordPage
from src.pages.logged_in_page import LoggedInPage
from src.pages.login_page import LoginPage
from src.pages.signup_page import SignupPage


class GitHubUI(BaseUIApp):
    """
    Use abstract methods to perform action on GitHub page.
    """

    def __init__(self, browser) -> None:
        super().__init__(browser)
        self.login_page = LoginPage(self)
        self.forgot_password_page = ForgotPasswordPage(self)
        self.signup_page = SignupPage(self)
        self.loggedin_page = LoggedInPage(self)

    def open_base_page(self) -> None:
        self.signup_page.go_to_page()

    def go_to_login_page(self) -> None:
        self.login_page.go_to_page()

    def go_to_forgot_password_page(self) -> None:
        self.forgot_password_page.go_to_page()

    def login_to_page(self, username: str, password: str) -> None:
        self.login_page.sign_in(username, password)

    def logout_off_page(self) -> None:
        """
        Logs off page by finding elements that are present if you are logged in.
        """
        self.loggedin_page.log_out()

    def find_element(self, locator_type: By, locator_name: str) -> bool:
        return self.get_element(locator_type, locator_name)

    def find_text(self, locator_type: By, locator_name: str) -> str:
        """
        Returns text found with given locator type and name.
        """
        self.wait_for_element_to_be_present(locator_type, locator_name)
        return self.get_element(locator_type, locator_name).text

    def search_in_github(self, text):
        self.signup_page.search_github(text)

    def type_email_you_forgot_password_for(self, text):
        self.forgot_password_page.type_email(text)

    def verify_reset_password_button_status(self):
        return self.forgot_password_page.reset_password_button_is_enabled()

    def close_current_browser(self):
        self.close_browser()
