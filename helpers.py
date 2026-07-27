import os
import json

class FileError(Exception):
    pass

def read_json_file(file_path):
    """Reads a JSON file and returns its content as a dictionary."""
    if not os.path.isfile(file_path):
        raise FileError(f"File not found: {file_path}")
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        raise FileError(f"Error decoding JSON from file: {file_path}")
    except Exception as e:
        raise FileError(f"An unexpected error occurred: {str(e)}")


def write_json_file(file_path, data):
    """Writes a dictionary to a JSON file."""
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary.")
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise FileError(f"Could not write to file: {file_path}. Error: {str(e)}")