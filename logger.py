import logging

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def log_info(message):
    """Logs an informational message."""
    logger.info(message)


def log_warning(message):
    """Logs a warning message."""
    logger.warning(message)


def log_error(message):
    """Logs an error message."""
    logger.error(message)


def log_debug(message):
    """Logs a debug message."""
    logger.debug(message)


def log_exception(exc):
    """Logs an exception with traceback."""
    logger.exception(exc)


def set_log_level(level):
    """Sets the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)."""
    level = level.upper()
    if level in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
        logger.setLevel(getattr(logging, level))
    else:
        logger.warning('Attempted to set invalid log level: %s', level)

