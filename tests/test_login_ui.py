import time

import pytest
from selenium.webdriver.common.by import By

from envs_config.secrets import GIT_PASSWORD
from src.config.config import config


def test_1_first_login_test(github_ui):
    github_ui.login_to_page(config.GIT_USERNAME, GIT_PASSWORD)
    logged_in = (
        github_ui.find_text(
            By.XPATH,
            "//h1[contains(text(), 'The home for all developers — including you.')]",
        )
        == "The home for all developers — including you."
    )
    github_ui.logout_off_page()
    logged_out = github_ui.find_text(By.LINK_TEXT, "Sign in") == "Sign in"
    assert logged_in == True
    assert logged_out == True


def test_2_failed_login_test(github_ui):
    github_ui.login_to_page(config.GIT_USERNAME, "not_a_password123")
    failed_login = (
        github_ui.find_text(
            By.XPATH, '//div[contains(text(), "Incorrect username or password.")]'
        )
        == "Incorrect username or password."
    )
    assert failed_login == True
