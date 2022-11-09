import json
import os
from typing import Any


class JSONConfigProvider:
    @staticmethod
    def _read_config(config_path):
        """
        Read the .json config and return it
        """
        with open(config_path) as json_file:
            return json.load(json_file)

    @staticmethod
    def get(item_name: str) -> Any:
        """
        Get the selected item (key) from json and return its value. Informs if json file does not exists
        """
        relative_path = os.path.dirname(__file__)
        json_relative_path = os.path.abspath(
            os.path.join(relative_path, "..", "..", "envs_config", "dev.json")
        )
        try:
            value = JSONConfigProvider._read_config(json_relative_path)
            return value.get(item_name)
        except FileNotFoundError:
            return f"{json_relative_path} does not exists."
