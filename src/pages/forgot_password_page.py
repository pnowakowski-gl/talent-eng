from selenium.webdriver.common.by import By

from src.config.config import config


class ForgotPasswordPage:
    FORGOT_PASSWORD_PAGE = "/password_reset"

    email_field = (By.ID, "email_field")
    send_password_reset_email = (
        By.XPATH,
        '//input[@value="Send password reset email"]',
    )

    def __init__(self, ui_app):
        self.ui_app = ui_app

    def go_to_page(self):
        self.ui_app.open_page(config.GITHUB_URL_UI + self.FORGOT_PASSWORD_PAGE)

    def type_email(self, text):
        self.ui_app.enter_text(*self.email_field, text)

    def reset_password_button_is_enabled(self):
        return self.ui_app.get_element(*self.send_password_reset_email).is_enabled()
