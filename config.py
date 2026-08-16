from typing import Dict, Any

class Config:
    """
    A class to store configuration settings.
    """
    def __init__(self, settings: Dict[str, Any]) -> None:
        """
        Initializes the Config with given settings.

        :param settings: A dictionary containing configuration settings.
        """
        self.settings = settings

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieves a setting by key.

        :param key: The key for the desired setting.
        :param default: The default value to return if the key is not found.
        :return: The setting value or the default.
        """
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Sets a value in the configuration.

        :param key: The key for the setting to update.
        :param value: The new value to set for the key.
        """
        self.settings[key] = value

    def remove(self, key: str) -> None:
        """
        Removes a setting by key.

        :param key: The key for the setting to remove.
        """
        self.settings.pop(key, None)

    def all_settings(self) -> Dict[str, Any]:
        """
        Returns all configuration settings.

        :return: A dictionary of all settings.
        """
        return self.settings