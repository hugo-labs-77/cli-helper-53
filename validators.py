import re

def validate_user_input(input_value):
    """Validates user input against predefined criteria."""
    if not isinstance(input_value, str):
        return False, 'Input must be a string.'
    if len(input_value) == 0:
        return False, 'Input cannot be empty.'
    if len(input_value) > 100:
        return False, 'Input exceeds maximum length of 100 characters.'
    if not re.match('^[a-zA-Z0-9_]+$', input_value):
        return False, 'Input can only contain alphanumeric characters and underscores.'
    return True, 'Input is valid.'

# Sample loop to demonstrate validation
if __name__ == '__main__':
    while True:
        user_input = input("Enter some input: ")
        valid, message = validate_user_input(user_input)
        print(message)
        if valid:
            break
