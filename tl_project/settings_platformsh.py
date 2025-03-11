import os
import platformshconfig
from pathlib import Path
from .settings import *

# Initialize Platform.sh configuration
config = platformshconfig.Config()

# Set debug mode
DEBUG = False

# Set secret key from environment
SECRET_KEY = os.environ.get('PLATFORM_PROJECT_ENTROPY', SECRET_KEY)

# Configure allowed hosts
ALLOWED_HOSTS = ['.platform.sh', '.platformsh.site']

# If we're on Platform.sh, get the configured domain
if config.is_valid_platform():
    ALLOWED_HOSTS.extend([
        config.get_primary_route().get('host', ''),
        f"www.{config.get_primary_route().get('host', '')}"
    ])

# Database configuration
if config.is_valid_platform():
    database_config = config.credentials('database')
    
    # Configure the database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': database_config['path'],
            'USER': database_config['username'],
            'PASSWORD': database_config['password'],
            'HOST': database_config['host'],
            'PORT': database_config['port'],
        }
    }

# Static files configuration
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/' 