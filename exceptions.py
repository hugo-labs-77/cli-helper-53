class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class ValidationError(CustomError):
    """Raised when a validation error occurs."""
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)

class NotFoundError(CustomError):
    """Raised when a requested resource is not found."""
    def __init__(self, resource_name: str) -> None:
        self.resource_name = resource_name
        message = f'Resource {resource_name} not found.'
        super().__init__(message)

class PermissionDeniedError(CustomError):
    """Raised when an action is not permitted."""
    def __init__(self, action: str) -> None:
        self.action = action
        message = f'Permission denied for action: {action}'
        super().__init__(message)

class ConfigurationError(CustomError):
    """Raised for configuration-related errors."""
    def __init__(self, config_item: str) -> None:
        self.config_item = config_item
        message = f'Configuration error with item: {config_item}'
        super().__init__(message)