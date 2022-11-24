import time

import pytest

from src.applications.githubApi import GitHubApi
from src.applications.githubUI import GitHubUI
from src.config.config import config
from src.models.sites import Sites


@pytest.fixture(scope="function")
def base_url_fixture():
    try:
        sites = Sites(config.BASE_URL)
        sites.add_to_database()

        yield sites

        sites.remove_from_database()
    except Exception as e:
        yield e


@pytest.fixture(scope="function")
def sql_fixture():
    try:
        sites = Sites(config.SQL_CONNECTION_STRING)
        sites.add_to_database()

        yield sites

        sites.remove_from_database()
    except Exception as e:
        yield e


@pytest.fixture(scope="function")
def get_repo_list():
    githubApi = GitHubApi()
    repositories_list = githubApi.get_list_of_public_repos("talent-eng")
    yield repositories_list


@pytest.fixture(scope="session")
def create_new_repo():
    githubApi = GitHubApi()
    add_repo = githubApi.create_new_repository(
        "new_repo", "new repo created via api call"
    )
    yield add_repo
    print(
        'Repository "new_repo" with description "new repo created via api call" was created.'
    )


@pytest.fixture(scope="session")
def delete_existing_repo():
    githubApi = GitHubApi()
    del_repo = githubApi.delete_existing_repository("new_repo")
    yield del_repo
    print('Repository "new_repo" was deleted.')


@pytest.fixture()
def github_ui(password):
    github_ui_app = GitHubUI()
    github_ui_app.open_base_page()
    github_ui_app.goto_login_page()
    time.sleep(3)
    github_ui_app.login_to_page(config.GIT_USERNAME, password)
    time.sleep(3)
    yield github_ui_app
