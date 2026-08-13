import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def divide_numbers(numerator, denominator):
    try:
        # Check types
        if not isinstance(numerator, (int, float)):
            raise TypeError('Numerator must be an int or float')
        if not isinstance(denominator, (int, float)):
            raise TypeError('Denominator must be an int or float')

        # Check for division by zero
        if denominator == 0:
            raise ValueError('Cannot divide by zero')

        result = numerator / denominator
        return result
    except TypeError as te:
        logger.error(f'Type error: {te}')
        return None  # or handle it as required
    except ValueError as ve:
        logger.error(f'Value error: {ve}')
        return None  # or handle it as required
    except Exception as e:
        logger.error(f'Unexpected error: {e}')
        return None  # or handle it as required


def safe_file_open(filename, mode='r'):
    try:
        with open(filename, mode) as file:
            return file.read()
    except FileNotFoundError:
        logger.error(f'File not found: {filename}')
        return None  # or handle it as required
    except IOError as e:
        logger.error(f'IO error: {e}')
        return None  # or handle it as required
    except Exception as e:
        logger.error(f'Unexpected error opening file: {e}')
        return None  # or handle it as required