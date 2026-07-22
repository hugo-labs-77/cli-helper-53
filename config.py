import os

# Application configuration settings
class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')
    DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')

# Security settings
class Security:
    CSRF_ENABLED = True
    CSRF_SECRET_KEY = os.environ.get('CSRF_SECRET_KEY', 'csrfsecret')

# Email configuration
class EmailConfig:
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true') == 'true'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', None)
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', None)

# Load configurations
def load_config():
    return {
        'debug': Config.DEBUG,
        'testing': Config.TESTING,
        'database_uri': Config.DATABASE_URI,
        'log_level': Config.LOG_LEVEL
    }