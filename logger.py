import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=5 * 1024 * 1024, backup_count=3):
    """
    Sets up a logger that writes log messages to a file with rotation.
    The log file will rotate when it exceeds max_bytes, keeping a number of backup files.
    """
    # Create a logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # Create a file handler that rotates the log files
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)

    # Create a console handler for output to terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(console_handler)

    return logger

# Example usage: Uncomment to test
# if __name__ == '__main__':
#     log = setup_logger()
#     log.debug('This is a debug message')
#     log.info('This is an info message')
#     log.warning('This is a warning message')
#     log.error('This is an error message')
#     log.critical('This is a critical message')