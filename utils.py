import os
import json

def read_json_file(file_path):
    """Reads a JSON file and returns its content."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json_file(file_path, data):
    """Writes the provided data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def cleanup_temp_files(temp_dir):
    """Removes temporary files from the specified directory."""
    if not os.path.exists(temp_dir):
        print(f"The directory {temp_dir} does not exist.")
        return
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Removed file: {file_path}")
        except Exception as e:
            print(f"Error removing {file_path}: {e}")


def list_directory_files(dir_path):
    """Returns a list of files in the specified directory."""
    return [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
