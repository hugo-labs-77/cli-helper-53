import json


def read_json(file_path):
    """
    Reads a JSON file and returns the data as a dictionary.
    :param file_path: Path to the JSON file.
    :return: Dictionary with the data from the JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON.")
        return {}


def write_json(file_path, data):
    """
    Writes a dictionary to a JSON file.
    :param file_path: Path where the JSON file will be written.
    :param data: The data to be written to the JSON file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        print(f"Error: Unable to write to file {file_path}.")


def update_json(file_path, new_data):
    """
    Updates a JSON file with new data.
    :param file_path: Path to the JSON file.
    :param new_data: Dictionary with new data to update.
    """
    existing_data = read_json(file_path)
    existing_data.update(new_data)
    write_json(file_path, existing_data)


def clear_json(file_path):
    """
    Clears the JSON file by writing an empty dictionary.
    :param file_path: Path to the JSON file.
    """
    write_json(file_path, {})