import pytest

from src.applications.githubApi import GitHubApi
from src.config.config import config
from src.models.sites import Sites

# CONSTS
REPO_NAME = "talent-eng"
REPO_TO_FIND = "pnowakowski-gl/talent-eng"
NEW_REPO = "new_repo"
NEW_REPO_DESC = "new repo created via api call"


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
def find_repo():
    githubApi = GitHubApi()
    search_repo = githubApi.search_repo(REPO_NAME)
    for i, name in enumerate(search_repo["items"]):
        print(name["full_name"])
        if name["full_name"] == REPO_TO_FIND:
            yield search_repo["items"][i]["id"]
            print("Repository found.")
            break
    else:
        yield None
        print("Repository not found")


@pytest.fixture(scope="class")
def create_new():
    githubApi = GitHubApi()
    add_repo = githubApi.create_repo(NEW_REPO, NEW_REPO_DESC)
    yield add_repo
    print(f'Repository {NEW_REPO} with description "{NEW_REPO_DESC}" was created.')


@pytest.fixture(scope="class")
def delete_existing():
    githubApi = GitHubApi()
    del_repo = githubApi.delete_repo(NEW_REPO)
    yield del_repo
    print(f"Repository {NEW_REPO} was deleted.")
