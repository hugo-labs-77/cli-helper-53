import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config = self.load_config(default_config_path)
        self.user_config = self.load_config(user_config_path)

    def load_config(self, config_path):
        if os.path.exists(config_path):
            with open(config_path, 'r') as file:
                return json.load(file)
        return {}

    def get_config(self):
        # Merge user config with defaults
        config = self.default_config.copy()
        config.update(self.user_config)
        return config

# Example of usage
if __name__ == '__main__':
    loader = ConfigLoader('default_config.json', 'user_config.json')
    config = loader.get_config()
    print(config)