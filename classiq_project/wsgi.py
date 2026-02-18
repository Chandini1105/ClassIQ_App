"""
WSGI config for classiq_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'classiq_project.settings')

application = get_wsgi_application()

# Optional: auto-create a default user in cloud environments
if os.environ.get("AUTO_CREATE_DEFAULT_USER", "").strip().lower() in ("1", "true", "yes", "y"):
    try:
        from allocation.utils.default_user import ensure_default_user

        ensure_default_user()
    except Exception:
        # Avoid crashing the app on startup for a non-critical helper
        pass

