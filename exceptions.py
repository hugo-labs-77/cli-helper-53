class CustomError(Exception):
    """
    Exception raised for custom errors.
    """

    def __init__(self, message: str) -> None:
        """
        Initializes CustomError with a message.
        
        :param message: Error message to display.
        """
        super().__init__(message)


class ValidationError(CustomError):
    """
    Exception raised for validation errors.
    """

    def __init__(self, field: str, message: str) -> None:
        """
        Initializes ValidationError with field and message.
        
        :param field: The name of the field that caused the error.
        :param message: The validation error message.
        """
        self.field = field
        super().__init__(message)


class NotFoundError(CustomError):
    """
    Exception raised when an item is not found.
    """

    def __init__(self, item_id: str) -> None:
        """
        Initializes NotFoundError with item ID.
        
        :param item_id: The ID of the item that was not found.
        """
        message = f"Item with ID '{item_id}' not found."
        super().__init__(message)


class UnauthorizedAccessError(CustomError):
    """
    Exception raised for unauthorized access attempts.
    """

    def __init__(self, user_id: str) -> None:
        """
        Initializes UnauthorizedAccessError with user ID.
        
        :param user_id: The ID of the user who attempted unauthorized access.
        """
        message = f"User with ID '{user_id}' is not authorized."
        super().__init__(message)