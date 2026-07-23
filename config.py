from typing import Any, Dict

class Config:
    """
    A simple configuration manager class that handles
    loading and accessing configuration settings.
    """
    def __init__(self, config: Dict[str, Any]) -> None:
        """
        Initializes the configuration with the provided dictionary.
        
        :param config: A dictionary containing configuration settings.
        """
        self.config = config

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieves the value associated with the given key.
        If the key does not exist, returns the default value.
        
        :param key: The key for the configuration setting.
        :param default: The value to return if the key is not found.
        :return: The value of the configuration setting or default value.
        """
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Sets the value for the given key in the configuration.
        
        :param key: The key for the configuration setting.
        :param value: The value to set for the configuration setting.
        """
        self.config[key] = value

    def remove(self, key: str) -> None:
        """
        Removes the key and its associated value from the configuration.
        
        :param key: The key to remove from the configuration.
        """
        self.config.pop(key, None)  

    def all(self) -> Dict[str, Any]:
        """
        Returns all configuration settings as a dictionary.
        
        :return: A dictionary of all configuration settings.
        """
        return self.config