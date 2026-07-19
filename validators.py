import re

def is_valid_email(email):
    """Check if the given email is valid."""
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.match(pattern, email) is not None


def is_positive_integer(value):
    """Check if the given value is a positive integer."""
    return isinstance(value, int) and value > 0


def is_valid_url(url):
    """Check if the given URL is valid."""
    pattern = r'^(http|https)://[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+(/.*)?$'
    return re.match(pattern, url) is not None


def is_non_empty_string(value):
    """Check if the given value is a non-empty string."""
    return isinstance(value, str) and bool(value.strip())


def validate_user_input(data):
    """Validate user input data based on certain criteria."""
    errors = []
    if not is_valid_email(data.get('email')):
        errors.append('Invalid email format.')
    if not is_positive_integer(data.get('age')):
        errors.append('Age must be a positive integer.')
    if not is_valid_url(data.get('website')):
        errors.append('Invalid URL format.')
    if not is_non_empty_string(data.get('username')):
        errors.append('Username cannot be empty.')

    return errors
