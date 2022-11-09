import os
from typing import Any


class OSConfigProvider:
    @staticmethod
    def get(item_name: str) -> Any:
        """
        Get enviroment variable key and return its value
        """
        value = os.getenv(item_name)
        return value
