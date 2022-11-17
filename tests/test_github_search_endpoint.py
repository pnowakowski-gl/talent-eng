import pytest

from src.applications.githubApi import GitHubApi

# CONSTS
MY_REPO_ID = 554665901
CREATED = 201
NO_CONTENT = 204

# TESTS
def test_repos_can_be_find(find_repo):
    assert find_repo == MY_REPO_ID


def test_repo_was_created(add_repo):
    assert add_repo == CREATED


def test_repo_was_deleted(delete_existing):
    assert delete_existing == NO_CONTENT
