import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file, max_bytes=1024 * 1024 * 5, backup_count=5):
    """Set up a logger with rotation."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    logger = setup_logger('app.log')
    logger.info('Logger setup complete.')