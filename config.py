import json
import os

class ConfigLoader:
    def __init__(self, default_config_path: str):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self) -> dict:
        if os.path.exists(self.default_config_path):
            with open(self.default_config_path, 'r') as config_file:
                return json.load(config_file)
        return {}

    def get(self, key: str, default=None):
        return self.config.get(key, default)

    def update(self, new_config: dict):
        self.config.update(new_config)

# Example usage
if __name__ == '__main__':
    config_loader = ConfigLoader('default_config.json')
    print(config_loader.get('some_key', 'default_value'))
    
