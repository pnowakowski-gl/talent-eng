import pytest

from src.applications.githubApi import GitHubApi
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
