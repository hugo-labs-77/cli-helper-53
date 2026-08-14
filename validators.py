from typing import Any, Dict, Optional


def validate_user_data(data: Dict[str, Any]) -> Optional[str]:
    """Validates user data dictionary.

    Args:
        data (Dict[str, Any]): Dictionary containing user data.

    Returns:
        Optional[str]: Error message if validation fails, otherwise None.
    """
    if not isinstance(data, dict):
        return 'Input must be a dictionary.'

    required_fields = ['username', 'email', 'age']
    for field in required_fields:
        if field not in data:
            return f'Missing required field: {field}'

    if not isinstance(data['username'], str) or len(data['username']) < 3:
        return 'Username must be a string with at least 3 characters.'

    if not isinstance(data['email'], str) or '@' not in data['email']:
        return 'Email must be a valid email address.'

    if not isinstance(data['age'], int) or data['age'] < 0:
        return 'Age must be a non-negative integer.'

    return None


def validate_product_data(data: Dict[str, Any]) -> Optional[str]:
    """Validates product data dictionary.

    Args:
        data (Dict[str, Any]): Dictionary containing product data.

    Returns:
        Optional[str]: Error message if validation fails, otherwise None.
    """
    if not isinstance(data, dict):
        return 'Input must be a dictionary.'

    required_fields = ['product_name', 'price', 'quantity']
    for field in required_fields:
        if field not in data:
            return f'Missing required field: {field}'

    if not isinstance(data['product_name'], str) or len(data['product_name']) == 0:
        return 'Product name must be a non-empty string.'

    if not isinstance(data['price'], (int, float)) or data['price'] < 0:
        return 'Price must be a non-negative number.'

    if not isinstance(data['quantity'], int) or data['quantity'] < 0:
        return 'Quantity must be a non-negative integer.'

    return None
