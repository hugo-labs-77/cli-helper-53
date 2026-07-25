'''Constants for the CLI Helper Application'''

# General application settings
APP_NAME = 'CLI Helper'
APP_VERSION = '1.0.0'
APP_AUTHOR = 'Your Name'

# Exit codes
EXIT_SUCCESS = 0
EXIT_FAILURE = 1

# Error messages
ERROR_MESSAGES = {
    'FILE_NOT_FOUND': 'The specified file was not found.',
    'INVALID_COMMAND': 'The command provided is invalid.',
    'PERMISSION_DENIED': 'You do not have permission to execute this operation.',
}

# Configuration constants
DEFAULT_CONFIG_PATH = './config/cli_helper_config.yaml'
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30

# Logging constants
LOGGING_LEVEL = 'DEBUG'
LOG_FILE_PATH = './logs/cli_helper.log'

# Command constants
COMMANDS = {
    'START': 'start',
    'STOP': 'stop',
    'RESTART': 'restart',
    'STATUS': 'status',
}

# Help and usage messages
HELP_MESSAGE = '''Usage: cli-helper [command] [options]
Commands:
    start    Start the CLI helper.
    stop     Stop the CLI helper.
    restart  Restart the CLI helper.
    status   Show the current status.
'''