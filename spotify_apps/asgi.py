"""
ASGI config for spotify_apps project
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotify_apps.settings')

application = get_asgi_application()
