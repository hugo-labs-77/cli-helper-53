import json
import os

DEFAULT_CONFIG = {
    'host': 'localhost',
    'port': 8000,
    'debug': True,
    'database_url': 'sqlite:///default.db'
}

class ConfigLoader:
    def __init__(self, config_path=None):
        self.config_path = config_path or 'config.json'
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as file:
                try:
                    user_config = json.load(file)
                    return {**DEFAULT_CONFIG, **user_config}
                except json.JSONDecodeError:
                    print(f'Error: Invalid JSON in {self.config_path}')
                    return DEFAULT_CONFIG
        return DEFAULT_CONFIG

    def get(self, key):
        return self.config.get(key, None)

if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.config)  # Print loaded configuration for debugging
