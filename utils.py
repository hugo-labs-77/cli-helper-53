import json
from typing import Any, Dict, List, Union

def load_json(file_path: str) -> Union[Dict[str, Any], List[Any]]:
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f'Error: The file {file_path} was not found.')
        return {}
    except json.JSONDecodeError:
        print(f'Error: Failed to decode JSON from the file {file_path}.')
        return {}


def save_json(file_path: str, data: Union[Dict[str, Any], List[Any]]) -> None:
    """Save data as JSON to a file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    except IOError:
        print(f'Error: Could not write to the file {file_path}.')


def update_dict(data: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
    """Update a dictionary with given updates."""
    data.update(updates)
    return data


def remove_key(data: Dict[str, Any], key: str) -> Dict[str, Any]:
    """Remove a key from a dictionary if it exists."""
    data.pop(key, None)
    return data
