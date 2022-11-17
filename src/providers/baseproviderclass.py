from typing import Any


class BaseProviderClass:
    @staticmethod
    def get(item_name: str) -> Any:
        """
        If get method is not implement it raises an error.
        """
        raise NotImplementedError("get method is not implemented")
