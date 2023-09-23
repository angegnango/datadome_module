# coding: utf-8
"""Configuration config file."""
from pathlib import Path
from functools import lru_cache
import configparser

CURRENT_PATH = Path(__file__).parent.parent


@lru_cache()
def get_configs():
    """."""
    config_object = configparser.ConfigParser()
    env_file_path = str(CURRENT_PATH / "config.ini")
    with open(env_file_path, "r") as file_object:
        config_object.read_file(file_object)
        return config_object
