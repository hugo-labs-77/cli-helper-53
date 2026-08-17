from typing import List, Dict, Any


def calculate_average(numbers: List[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (List[float]): A list of numbers to average.

    Returns:
        float: The average of the numbers.
    """
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    return sum(numbers) / len(numbers)


def flatten_dict(nested_dict: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """
    Flatten a nested dictionary into a flat dictionary.

    Args:
        nested_dict (Dict[str, Any]): The nested dictionary to flatten.
        parent_key (str, optional): The base key to prefix to the keys in the flattened dictionary. Defaults to ''.
        sep (str, optional): The separator to use between keys. Defaults to '.'.

    Returns:
        Dict[str, Any]: A flat dictionary.
    """
    items = []
    for k, v in nested_dict.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)