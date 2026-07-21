import os
import json
import logging

def load_json(file_path):
    """Load a JSON file and return its content."""
    if not os.path.isfile(file_path):
        logging.error(f'File not found: {file_path}')
        return None
    with open(file_path, 'r') as json_file:
        try:
            return json.load(json_file)
        except json.JSONDecodeError as e:
            logging.error(f'Error decoding JSON: {e}')
            return None


def save_json(data, file_path):
    """Save data to a JSON file."""
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        logging.info(f'Data saved to {file_path}')


def get_file_extension(file_name):
    """Return the file extension from a filename."""
    return os.path.splitext(file_name)[1]


# Example usage
if __name__ == '__main__':
    data = load_json('example.json')
    if data:
        save_json(data, 'output.json')
    ext = get_file_extension('document.txt')
    print(f'File extension: {ext}')