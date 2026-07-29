import os

# Configuration class to handle application settings
class Config:
    # Application settings
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///app.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    API_VERSION = 'v1'

    @classmethod
    def init_app(cls, app):
        # Initialize app with config settings
        app.config.from_object(cls)
        
    @classmethod
    def get_database_uri(cls):
        # Return the database URI
        return cls.DATABASE_URI

    @classmethod
    def is_debug_mode(cls):
        # Check if the application is in debug mode
        return cls.DEBUG