import json
from typing import Any, Dict, List, Union

def load_json(file_path: str) -> Union[Dict[str, Any], List[Any]]:
    """Load JSON data from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json(data: Union[Dict[str, Any], List[Any]], file_path: str) -> None:
    """Save JSON data to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries into one."""
    merged = dict1.copy()  # Make a copy of the first dictionary
    merged.update(dict2)   # Update with the second dictionary
    return merged


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """Flatten a nested list."""
    return [item for sublist in nested_list for item in sublist]
