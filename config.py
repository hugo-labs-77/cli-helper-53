import os
import json

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            raise ConfigError(f'Config file not found: {self.config_file}')
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            raise ConfigError('Error decoding JSON from the config file')
        except Exception as e:
            raise ConfigError(f'Unexpected error: {str(e)}')

    def get(self, key, default=None):
        return self.config_data.get(key, default)

# Example usage of the Config class if needed:
# config = Config('config.json')
# print(config.get('some_key', 'default_value'))
