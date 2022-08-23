"""
WSGI config for familyexpress project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os, sys
# add the hellodjango project path into the sys.path
sys.path.append('/home/oem/familyexpress/')
# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/oem/familyexpress/venv/lib/python3.8/site-packages')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'familyexpress.settings')

application = get_wsgi_application()
