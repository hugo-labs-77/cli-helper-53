def validate_input(user_input):
    """Validates the user's input against a set of predefined criteria."""
    if not user_input:
        raise ValueError("Input cannot be empty.")
    if not isinstance(user_input, str):
        raise TypeError("Input must be a string.")
    if len(user_input) < 3:
        raise ValueError("Input must be at least 3 characters long.")
    if user_input.isdigit():
        raise ValueError("Input cannot be entirely numeric.")
    return True

# Example usage within a main processing loop
if __name__ == '__main__':
    while True:
        try:
            user_input = input('Enter some text: ')
            validate_input(user_input)
            print(f'Valid input: {user_input}')
            break
        except (ValueError, TypeError) as e:
            print(f'Error: {e}')