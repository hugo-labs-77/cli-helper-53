import logging
import logging.handlers


def setup_logger(log_file:str, max_bytes:int=10485760, backup_count:int=5) -> logging.Logger:
    """Set up a logger with rotating file handler."""
    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Set the logging level

    # Create a file handler that logs messages to a file
    file_handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)  
    file_handler.setLevel(logging.DEBUG)  # Set the level for the file handler

    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)
    return logger


if __name__ == '__main__':
    # Example of usage
    my_logger = setup_logger('app.log')
    my_logger.info('Logger has been set up!')
    my_logger.warning('This is a warning message!')
