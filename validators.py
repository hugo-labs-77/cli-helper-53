def validate_input(user_input):
    """
    Validate user input to ensure it meets specified criteria.
    Returns True if valid, otherwise raises ValueError.
    """
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string.")
    if len(user_input) == 0:
        raise ValueError("Input cannot be empty.")
    if not user_input.isalnum():
        raise ValueError("Input must be alphanumeric.")
    return True

if __name__ == '__main__':
    while True:
        user_input = input("Enter your input: ")
        try:
            validate_input(user_input)
            print("Input is valid!")
            break  # Exit loop on valid input
        except ValueError as e:
            print(f"Invalid input: {e}")
