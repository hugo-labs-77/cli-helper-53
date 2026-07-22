import os
import json
import hashlib

def read_json_file(file_path):
    """Reads a JSON file and returns its contents as a dictionary."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error reading {file_path}: {e}')
        return None

def write_json_file(file_path, data):
    """Writes a dictionary to a JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f'Error writing to {file_path}: {e}')


def hash_string(input_string):
    """Returns the SHA-256 hash of a string."""
    return hashlib.sha256(input_string.encode()).hexdigest()


def ensure_directory_exists(dir_path):
    """Creates a directory if it does not exist."""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f'Directory created: {dir_path}')
    else:
        print(f'Directory already exists: {dir_path}')