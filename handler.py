import json

class CLIHelper:
    def __init__(self):
        self.data = {}

    def load_json(self, filepath):
        """Load JSON data from a file."""
        try:
            with open(filepath, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f'Error: {filepath} not found.')
        except json.JSONDecodeError:
            print('Error: Failed to decode JSON.')

    def save_json(self, filepath):
        """Save data to a JSON file."""
        try:
            with open(filepath, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError:
            print('Error: Unable to write to file.')

    def get_data(self, key):
        """Retrieve value by key from loaded JSON data."""
        return self.data.get(key, 'Key not found')

    def set_data(self, key, value):
        """Set a value by key in the JSON data."""
        self.data[key] = value

    def display_data(self):
        """Print the current data in a readable format."""
        print(json.dumps(self.data, indent=4))

# Example usage:
# cli_helper = CLIHelper()
# cli_helper.load_json('data.json')
# cli_helper.display_data()
# cli_helper.set_data('new_key', 'new_value')
# cli_helper.save_json('data.json')