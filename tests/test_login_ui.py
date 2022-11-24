import time

import pytest
from selenium.webdriver.common.by import By

from envs_config.secrets import GIT_PASSWORD


@pytest.mark.parametrize("password", [GIT_PASSWORD])
def test_1_first_login_test(github_ui):
    logged_in = github_ui.check_if_text_is_present(
        By.XPATH,
        "//h1[contains(text(), 'The home for all developers — including you.')]",
    )
    time.sleep(3)
    github_ui.logout_off_page()
    time.sleep(3)
    logged_out = github_ui.check_if_text_is_present(By.LINK_TEXT, "Sign in")
    assert logged_in == "The home for all developers — including you."
    assert logged_out == "Sign in"


@pytest.mark.parametrize("password", ["not_a_password123"])
def test_2_failed_login_test(github_ui):
    failed_login = github_ui.check_if_text_is_present(
        By.XPATH, '//*[@id="js-flash-container"]/div/div/div'
    )
    assert failed_login == "Incorrect username or password.  "
