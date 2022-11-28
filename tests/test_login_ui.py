import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.config.config import config
from src.pages.logged_in_page import LoggedInPage
from src.pages.login_page import LoginPage
from src.pages.signup_page import SignupPage


def test_1_successful_login(github_ui):
    github_ui.go_to_login_page()
    github_ui.login_to_page(config.GIT_USERNAME, config.GIT_PASSWORD)
    logged_in = github_ui.find_element(*LoggedInPage.logged_in_avatar)
    print(logged_in)
    assert isinstance(logged_in, WebElement)


def test_2_failed_login_test(github_ui):
    github_ui.go_to_login_page()
    github_ui.login_to_page(config.GIT_USERNAME, "not_a_password123")
    failed_login_text = github_ui.find_text(*LoginPage.incorrect_password_msg)
    assert failed_login_text == "Incorrect username or password."


def test_3_log_out(github_ui):
    github_ui.go_to_login_page()
    github_ui.login_to_page(config.GIT_USERNAME, config.GIT_PASSWORD)
    github_ui.find_element(*LoggedInPage.logged_in_avatar)
    github_ui.logout_off_page()
    logged_out_text = github_ui.find_text(*SignupPage.sign_in_)
    assert logged_out_text == "Sign in"


def test_4_search(github_ui):
    github_ui.search_in_github("testing search")
    el = github_ui.find_element(
        By.XPATH,
        '//div[@class="d-flex flex-column flex-md-row flex-justify-between border-bottom pb-3 position-relative"]',
    )
    assert isinstance(el, WebElement)


def test_5_forgot_password(github_ui):
    github_ui.go_to_forgot_password_page()
    github_ui.type_email_you_forgot_password_for("default@email.com")
    assert github_ui.verify_reset_password_button_status() is False
