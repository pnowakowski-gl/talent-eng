from typing import Any
from config_provider import JSONConfigProvider, OSConfigProvider


class Config:
    """
    Holds all the settings of the framework.
    Parameter is list of config providers.
    """

    def __init__(self, config_providers: list) -> None:
        self.config_providers = config_providers
        self.conf_dict = {}
        self.keys_to_register = ["BASE_URL", "SQL_CONNECTION_STRING"]

        for key in self.keys_to_register:
            self._register(key)

    def get(self, item_name: str) -> Any:
        """
        Gets value of a key from config dictionary and returns it.
        """
        try:
            return self.conf_dict[item_name]
        except KeyError:
            return f"{item_name} is missing in a config."

    def _register(self, item_name: str) -> None:
        """
        Iterate through list of config providers to search for key and append it to configuration
        dictionary if it has a value.
        """
        for provider in self.config_providers:
            value = provider.get(item_name)
            if value is not None:
                self.conf_dict[item_name] = value
                return

config = Config([OSConfigProvider, JSONConfigProvider])
print(config.get("BASE_URL"))
print(config.get("SQL_CONNECTION_STRING"))
print(config.get("BASE_URLS"))
print(config.get("SQL_CONNECTION_STRINGS"))

