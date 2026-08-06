class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class ValidationError(CustomError):
    """Raised when a validation error occurs."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class DatabaseError(CustomError):
    """Raised when a database error occurs."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NotFoundError(CustomError):
    """Raised when a requested item is not found."""
    def __init__(self, entity):
        self.message = f'{entity} not found'
        super().__init__(self.message)

class AuthenticationError(CustomError):
    """Raised when authentication fails."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)