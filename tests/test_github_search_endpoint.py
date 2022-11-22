import pytest

# CONSTS
MY_REPO_ID = 554665901
CREATED = 201
NO_CONTENT = 204
OWNER_LOGIN = "showroomotomotif"
OWNER_ID = 86302521

# TESTS
def test_1_repos_can_be_find(get_repo_list):
    id = None
    for i, repo in enumerate(get_repo_list["items"]):
        if repo["full_name"] == "pnowakowski-gl/talent-eng":
            id = get_repo_list["items"][i]["id"]
            print("Repository found.")
            break
    assert id == MY_REPO_ID


def test_2_repos_can_be_find(get_repo_list):
    owner_login = None
    owner_id = None
    for i, repo in enumerate(get_repo_list["items"]):
        if repo["id"] == 380071073:
            owner_login = get_repo_list["items"][i]["owner"]["login"]
            print("Owner's login found.")
            owner_id = get_repo_list["items"][i]["owner"]["id"]
            print("Owner's id found.")
            break
    assert owner_login == OWNER_LOGIN
    assert owner_id == OWNER_ID


def test_3_repo_was_created(create_new_repo):
    assert create_new_repo == CREATED


def test_4_repo_was_deleted(delete_existing_repo):
    assert delete_existing_repo == NO_CONTENT
