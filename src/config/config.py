import os
from typing import Any

from dotenv import load_dotenv

from src.providers.jsonconfigprovider import JSONConfigProvider
from src.providers.osconfigprovider import OSConfigProvider


class Config:
    """
    Holds all the settings of the framework.
    Parameter is list of config providers.
    """

    def __init__(self, config_providers: list) -> None:
        self._load_secrets()
        self.config_providers = config_providers
        self.conf_dict = {}
        self.keys_to_register = [
            "BASE_URL",
            "SQL_CONNECTION_STRING",
            "NOSQL_CONNECTION_STRING",
            "GITHUB_URL_API",
            "GITHUB_URL_UI",
            "GIT_USERNAME",
            "GIT_API_KEY",
            "GIT_PASSWORD",
        ]

        for key in self.keys_to_register:
            self._register(key)

    def __getattr__(self, item_name: str) -> Any:
        try:
            return self.conf_dict[item_name]
        except KeyError:
            return f"{item_name} is not in the configuration dictionary."

    def _register(self, item_name: str) -> None:
        """
        Iterate through list of config providers to search for key and append it to configuration
        dictionary if it has a value. Raise value error if the key is registered by is missing
        in a config.
        """
        for provider in self.config_providers:
            value = provider.get(item_name)
            if value is not None:
                self.conf_dict[item_name] = value
                return

        raise ValueError(f"{item_name} is missing in a config.")

    def _load_secrets(self):
        relative_path = os.path.dirname(__file__)
        secrets_path = os.path.abspath(os.path.join(relative_path, "..", "..", "envs_config", "secrets.env"))
        load_dotenv(dotenv_path=secrets_path)


config = Config([OSConfigProvider, JSONConfigProvider])
