import logging

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # Create console handler and set level to debug
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        # Add handler to logger
        self.logger.addHandler(handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

# Usage example
if __name__ == '__main__':
    log = Logger('my_logger')
    log.info('This is an info message')
    log.error('This is an error message')
