"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

# ADD YOUR PROJECT TO THE PYTHONPATH FOR THE PYTHON INSTANCE
path = '/home/SubrataSarkar32/mysite'

if path not in sys.path:
    sys.path.append(path)

os.chdir(path)

# TELL DJANGO WHERE YOUR SETTINGS MODULE IS LOCATED
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# IMPORT THE whitenoise DJANGO WSGI HANDLER TO TAKE CARE OF REQUESTS
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
