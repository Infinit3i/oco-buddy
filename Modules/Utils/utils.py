import json
import os


def ensure_directory_exists(directory):
    """
    Ensures that a directory exists. Creates it if not.
    :param directory: Path to the directory.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)


def save_action_status(file_path, action_status):
    """
    Saves the action status dictionary to a JSON file.
    :param file_path: Path to the JSON file.
    :param action_status: Dictionary of action statuses to save.
    """
    with open(file_path, "w") as f:
        json.dump(action_status, f, indent=4)


def load_action_status(file_path, default=None):
    """
    Loads the action status dictionary from a JSON file.
    If the file does not exist, returns the default value.
    :param file_path: Path to the JSON file.
    :param default: Default value to return if the file does not exist.
    :return: Dictionary of action statuses.
    """
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return default or {}
