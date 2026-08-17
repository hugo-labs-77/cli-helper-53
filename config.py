import json
import os

class ConfigLoader:
    def __init__(self, default_config_path: str):
        self.default_config_path = default_config_path
        self.config = self.load_defaults()

    def load_defaults(self) -> dict:
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def load_custom_config(self, custom_config_path: str) -> None:
        if os.path.exists(custom_config_path):
            with open(custom_config_path, 'r') as file:
                custom_config = json.load(file)
                self.config.update(custom_config)

    def get_config(self) -> dict:
        return self.config

# Example usage:
# config_loader = ConfigLoader('defaults.json')
# config_loader.load_custom_config('custom.json')
# config = config_loader.get_config()  
