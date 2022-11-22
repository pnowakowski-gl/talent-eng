import pytest
import requests

# CONSTS
BASE_URL = "http://google.com"
DB_SIZE = 1
REQUESTS_EXCEPTIONS = requests.exceptions.HTTPError('No connection found')


# TESTS
def test_1_base_url_added_and_appended_to_list(base_url_fixture):
    print(f"BASE_URL status code is {base_url_fixture.status_code}.")
    assert len(base_url_fixture.sites_list) == DB_SIZE
    assert base_url_fixture.sites_list[-1] == BASE_URL


def test_2_base_url_check_scope(base_url_fixture):
    print(f"BASE_URL status code is {base_url_fixture.status_code}.")
    assert len(base_url_fixture.sites_list) == DB_SIZE


def test_3_sql_check_connection(sql_fixture):
    print("Checking SQL connection.")
    assert type(sql_fixture) == type(REQUESTS_EXCEPTIONS)
    assert sql_fixture.args == REQUESTS_EXCEPTIONS.args