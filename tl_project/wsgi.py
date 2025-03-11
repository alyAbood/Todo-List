"""
WSGI config for tl_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys
import platformshconfig

from django.core.wsgi import get_wsgi_application

# Check if we're on Platform.sh
config = platformshconfig.Config()
if config.is_valid_platform():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tl_project.settings_platformsh')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tl_project.settings')

application = get_wsgi_application()
