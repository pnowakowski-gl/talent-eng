from selenium.webdriver.common.by import By

from src.config.config import config


class LoginPage:
    LOGIN_PAGE = "/login"

    username_field = (By.ID, "login_field")
    password_field = (By.ID, "password")
    sign_in_button = (By.NAME, "commit")
    forgot_password = (By.XPATH, '//a[contains(text(), "Forgot password?")]')
    create_an_account = (By.XPATH, '//a[contains(text(), "Create an account")]')
    incorrect_password_msg = (
        By.XPATH,
        '//div[contains(text(), "Incorrect username or password.")]',
    )

    def __init__(self, ui_app):
        self.ui_app = ui_app

    def go_to_page(self):
        self.ui_app.open_page(config.GITHUB_URL_UI + self.LOGIN_PAGE)

    def sign_in(self, username: str, password: str) -> None:
        self.ui_app.wait_for_element_to_be_present(*self.username_field)
        self.ui_app.enter_text(*self.username_field, username)
        self.ui_app.enter_text(*self.password_field, password)
        self.ui_app.click(*self.sign_in_button)

    def go_to_forgot_password_page(self):
        self.ui_app.click(*self.forgot_password)

    def go_to_create_an_account_page(self):
        self.ui_app.click(*self.create_an_account)
