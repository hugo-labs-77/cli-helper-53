import logging


def setup_logger(name):
    """
    Setup a logger with a given name.
    Includes StreamHandler for console output.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # Add handler to the logger
    logger.addHandler(ch)
    return logger


def log_info(logger, message):
    """
    Log an informational message.
    """
    logger.info(message)


def log_warning(logger, message):
    """
    Log a warning message.
    """
    logger.warning(message)


def log_error(logger, message):
    """
    Log an error message.
    """
    logger.error(message)


def log_critical(logger, message):
    """
    Log a critical error message.
    """
    logger.critical(message)