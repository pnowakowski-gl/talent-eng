import pytest

from src.config.config import config
from src.models.sites import Sites


@pytest.fixture(scope="class")
def base_url_fixture():
    sites = Sites(config.BASE_URL)
    added = sites.add_to_database()

    yield sites, added

    sites.remove_from_database()


@pytest.fixture(scope="function")
def sql_fixture():
    sites = Sites(config.SQL_CONNECTION_STRING)
    sites.add_to_database()

    yield sites

    sites.remove_from_database()
