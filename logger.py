import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=3):
    # Create a logger with the specified name
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)  # Set log level to DEBUG

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

# Example usage
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger is set up with rotation')
    log.debug('This is a debug message')
    log.warning('This is a warning message')
    log.error('This is an error message')
    log.critical('This is a critical message')