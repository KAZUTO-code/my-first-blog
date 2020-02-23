"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from .local_settings import *

if DEBUG == False:
    import sys
    sys.path.append('/var/www/environments/my-first-blog')
    sys.path.append('/var/www/environments/my-first-blog/mysite')
    sys.path.append('/usr/lib/python3.7/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
