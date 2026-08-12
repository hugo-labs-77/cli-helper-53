import json
import os

class ConfigLoader:
    def __init__(self, default_config_file='defaults.json'):
        self.config = self.load_defaults(default_config_file)

    def load_defaults(self, default_config_file):
        if not os.path.exists(default_config_file):
            raise FileNotFoundError(f'Default configuration file {default_config_file} not found.')
        with open(default_config_file, 'r') as file:
            return json.load(file)

    def load_custom(self, custom_config_file):
        if os.path.exists(custom_config_file):
            with open(custom_config_file, 'r') as file:
                custom_config = json.load(file)
            self.config.update(custom_config)
        else:
            raise FileNotFoundError(f'Custom configuration file {custom_config_file} not found.')

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage
if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.get('some_key', 'default_value'))