from src.config.config import config
from src.models.sites import Sites
import pytest

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