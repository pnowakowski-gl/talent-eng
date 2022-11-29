import pytest

from src.config.config import config


def test_1_successful_login(github_ui):
    github_ui.go_to_login_page()
    github_ui.login_to_page(config.GIT_USERNAME, config.GIT_PASSWORD)
    assert github_ui.user_is_logged_in() is True


def test_2_failed_login_test(github_ui):
    github_ui.go_to_login_page()
    github_ui.login_to_page(config.GIT_USERNAME, "not_a_password123")
    assert github_ui.incorrect_credentials_text() == "Incorrect username or password."


def test_3_log_out(github_ui):
    github_ui.go_to_login_page()
    github_ui.login_to_page(config.GIT_USERNAME, config.GIT_PASSWORD)
    github_ui.user_is_logged_in()
    github_ui.logout_off_page()
    assert github_ui.sign_in_button_is_present() is True


def test_4_search(github_ui):
    assert github_ui.github_search_is_working() is True


def test_5_forgot_password(github_ui):
    github_ui.go_to_forgot_password_page()
    github_ui.type_email_you_forgot_password_for("default@email.com")
    assert github_ui.verify_reset_password_button_status() is False
