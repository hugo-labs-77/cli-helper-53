import sys
import re

def is_valid_input(user_input):
    # Validate input to ensure it's alphanumeric
    return bool(re.match('^[a-zA-Z0-9]+$', user_input))

def main_loop():
    while True:
        user_input = input('Enter alphanumeric input (or type "exit" to quit): ')
        if user_input.lower() == 'exit':
            print('Exiting the program. Goodbye!')
            break
        if not is_valid_input(user_input):
            print('Invalid input. Please enter only alphanumeric characters.')
            continue
        # Process valid input
        print(f'You entered: {user_input}')

if __name__ == '__main__':
    main_loop()