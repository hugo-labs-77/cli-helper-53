class CustomError(Exception):
    """Base class for custom exceptions in this module."""
    pass

class ValidationError(CustomError):
    """Exception raised for validation errors."""
    def __init__(self, message, field):
        self.message = message
        self.field = field
        super().__init__(self.message)

class DataNotFoundError(CustomError):
    """Exception raised when required data is not found."""
    def __init__(self, data_key):
        self.data_key = data_key
        self.message = f'Data not found for key: {self.data_key}'
        super().__init__(self.message)

class PermissionError(CustomError):
    """Exception raised for permission-related issues."""
    def __init__(self, user, action):
        self.user = user
        self.action = action
        self.message = f'User {self.user} does not have permission to {self.action}'
        super().__init__(self.message)
