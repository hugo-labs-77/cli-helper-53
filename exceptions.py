class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class ValidationError(CustomError):
    """Raised when validation fails."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NotFoundError(CustomError):
    """Raised when a requested resource is not found."""
    def __init__(self, resource):
        self.resource = resource
        self.message = f'{resource} not found'
        super().__init__(self.message)

class PermissionError(CustomError):
    """Raised when action is not allowed."""
    def __init__(self, action):
        self.action = action
        self.message = f'Permission denied for {action}'
        super().__init__(self.message)