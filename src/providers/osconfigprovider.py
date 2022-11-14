import os
from typing import Any
from src.providers.baseproviderclass import BaseProviderClass

class OSConfigProvider(BaseProviderClass):
    @staticmethod
    def get(item_name: str) -> Any:
        """
        Get enviroment variable key and return its value
        """
        value = os.getenv(item_name)
        return value
