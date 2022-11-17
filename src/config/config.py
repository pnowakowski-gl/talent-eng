from typing import Any

from src.providers.jsonconfigprovider import JSONConfigProvider
from src.providers.osconfigprovider import OSConfigProvider


class Config:
    """
    Holds all the settings of the framework.
    Parameter is list of config providers.
    """

    def __init__(self, config_providers: list) -> None:
        self.config_providers = config_providers
        self.conf_dict = {}
        self.keys_to_register = [
            "BASE_URL",
            "SQL_CONNECTION_STRING",
            "NOSQL_CONNECTION_STRING",
            "GITHUB_URL",
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


config = Config([OSConfigProvider, JSONConfigProvider])
