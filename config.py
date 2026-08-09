# Configuration for the application

# Base directory of the application
BASE_DIR = '/path/to/application'

# Logging configuration
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{'
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Database configuration
DATABASE_CONFIG = {
    'engine': 'django.db.backends.sqlite3',
    'name': BASE_DIR + '/db.sqlite3',
}

# API configuration
API_CONFIG = {
    'base_url': 'https://api.example.com',
    'timeout': 30,
}
