import os
from pathlib import Path
from .settings import *

# Try to import platformshconfig, but handle the case when it's not available
try:
    import platformshconfig
    # Initialize Platform.sh configuration
    config = platformshconfig.Config()
    
    # Set debug mode
    DEBUG = False
    
    # Set secret key from environment
    SECRET_KEY = os.environ.get('PLATFORM_PROJECT_ENTROPY', SECRET_KEY)
    
    # Configure allowed hosts - allow all hosts for now to troubleshoot
    ALLOWED_HOSTS = ['*']
    
    # If we're on Platform.sh, add the routes to allowed hosts
    if config.is_valid_platform():
        # Add all Platform.sh routes to allowed hosts
        routes = config.routes
        for route_url, route_info in routes.items():
            host = route_info.get('host', '')
            if host:
                ALLOWED_HOSTS.append(host)
                # Also add the www subdomain if it exists
                if host.startswith('www.'):
                    continue
                ALLOWED_HOSTS.append(f"www.{host}")
    
    # Database configuration
    if config.is_valid_platform():
        try:
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
        except Exception as e:
            print(f"Database configuration error: {e}")
            
except ImportError:
    # Not on Platform.sh or package not installed
    print("Platform.sh config not available, using default settings")
    # You can set fallback values here if needed

# Static files configuration (applies regardless of environment)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/' 