import os
import logging

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

logger = logging.getLogger(__name__)

class EmailBackend(ModelBackend):
    """Custom authentication backend to support email login with @cmr.edu.in"""
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            return None

        normalized = username.strip()
        if not normalized:
            return None

        try:
            # Try to get user by email (case-insensitive)
            user = User.objects.get(email__iexact=normalized)
        except User.DoesNotExist:
            try:
                # Fallback to username (case-insensitive)
                user = User.objects.get(username__iexact=normalized)
            except User.DoesNotExist:
                user = None

        if user is None:
            # Optional: auto-provision users for @cmr.edu.in with default password
            if (
                os.environ.get("AUTO_PROVISION_USERS", "").strip().lower() in ("1", "true", "yes", "y")
                and normalized.lower().endswith("@cmr.edu.in")
                and password == os.environ.get("DEFAULT_LOGIN_PASSWORD", "CMRU 1")
            ):
                user = User.objects.create_user(
                    username=normalized.lower(),
                    email=normalized.lower(),
                    password=password,
                )
                logger.info("Auto-provisioned user: %s", normalized)
            else:
                return None

        # Check password
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
