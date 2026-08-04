import sys

# This function validates user input
def validate_input(user_input):
    if not isinstance(user_input, str) or len(user_input) == 0:
        raise ValueError('Input must be a non-empty string')
    return user_input

# Main processing loop
def main_loop():
    while True:
        try:
            user_input = input('Enter a command: ')  # Get user input
            validated_input = validate_input(user_input)  # Validate input
            # Process the validated input
            print(f'Processing command: {validated_input}')  
        except ValueError as e:
            print(f'Error: {e}')  # Handle validation errors
        except KeyboardInterrupt:
            print('\nTerminating the program. Goodbye!')
            sys.exit(0)  # Graceful exit on Ctrl+C

if __name__ == '__main__':
    main_loop()