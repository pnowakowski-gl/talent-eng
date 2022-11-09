import pytest


def test_1_base_url_added_and_appended_to_list(base_url_fixture):
    url, added = base_url_fixture
    print(f"BASE_URL status code is {url.status_code}.")
    assert added == True
    assert url.sites_list[-1] == "http://google.com"
    url.remove_from_database()


def test_2_base_url_check_scope(base_url_fixture):
    url, _ = base_url_fixture
    print(f"BASE_URL status code is {url.status_code}.")
    assert len(url.sites_list) == 1


@pytest.mark.xfail
def test_3_sql_check_connection(sql_fixture):
    print("Checking SQL connection.")
    assert sql_fixture.status_code == 200
