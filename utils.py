from typing import List, Dict, Any


def safe_get(dictionary: Dict[str, Any], key: str, default: Any = None) -> Any:
    """
    Get a value from a dictionary safely.

    Args:
        dictionary (Dict[str, Any]): The dictionary to retrieve the value from.
        key (str): The key to search for.
        default (Any, optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Any: The value associated with the key, or the default value if not found.
    """
    return dictionary.get(key, default)


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """
    Flatten a nested list.

    Args:
        nested_list (List[List[Any]]): A list of lists to flatten.

    Returns:
        List[Any]: A single flattened list containing all the elements.
    """
    return [item for sublist in nested_list for item in sublist]


def merge_dictionaries(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two dictionaries into one.

    Args:
        dict1 (Dict[str, Any]): The first dictionary.
        dict2 (Dict[str, Any]): The second dictionary.

    Returns:
        Dict[str, Any]: A new dictionary containing keys and values from both dictionaries.
    """
    merged = dict1.copy()  # Copying the first dictionary
    merged.update(dict2)  # Updating with the second dictionary
    return merged
