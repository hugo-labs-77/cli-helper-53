import logging
from logging.handlers import RotatingFileHandler

# Setting up the logger

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=3):
    """
    Configures a logger with a rotating file handler.
    :param log_file: Path to the log file
    :param max_bytes: Max size of log file before rotation
    :param backup_count: Number of backup files to keep
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set the logging level

    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger.addHandler(handler)
    return logger

# Usage example
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger is set up and ready to use.')