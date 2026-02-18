import os
import logging

from django.contrib.auth import get_user_model
from django.db.utils import OperationalError, ProgrammingError

logger = logging.getLogger(__name__)

DEFAULT_PASSWORD = "CMRU 1"


def _truthy(value: str) -> bool:
    if not value:
        return False
    normalized = value.strip().lower()
    return normalized not in ("0", "false", "no", "n", "off")


def ensure_default_user() -> None:
    """Create a default user once when running in cloud, if configured."""
    email = os.environ.get("DEFAULT_LOGIN_EMAIL", "").strip()
    if not email:
        logger.warning("DEFAULT_LOGIN_EMAIL not set; skipping default user creation")
        return

    if "email ending" in email.lower():
        logger.warning("DEFAULT_LOGIN_EMAIL appears to be a placeholder value: %s", email)
        return

    # Enforce cmr.edu.in domain to match project auth rules
    if not email.lower().endswith("@cmr.edu.in"):
        logger.warning("DEFAULT_LOGIN_EMAIL must end with @cmr.edu.in, got: %s", email)
        return

    password = os.environ.get("DEFAULT_LOGIN_PASSWORD", DEFAULT_PASSWORD)
    name = os.environ.get("DEFAULT_LOGIN_NAME", "CMRU User")
    reset_password = _truthy(os.environ.get("DEFAULT_LOGIN_RESET_PASSWORD", ""))

    try:
        User = get_user_model()
        existing = (
            User.objects.filter(email__iexact=email).first()
            or User.objects.filter(username__iexact=email).first()
        )
        if existing:
            if reset_password:
                existing.set_password(password)
                existing.save(update_fields=["password"])
                logger.info("Default user password reset for %s", email)
            else:
                logger.info("Default user already exists: %s", email)
            return

        user = User.objects.create_user(
            username=email.lower(),
            email=email.lower(),
            password=password,
        )
        logger.info("Default user created: %s", email)

        # Set optional flags when provided
        if _truthy(os.environ.get("DEFAULT_LOGIN_IS_STAFF", "")):
            user.is_staff = True
        if _truthy(os.environ.get("DEFAULT_LOGIN_IS_SUPERUSER", "")):
            user.is_superuser = True

        # Best-effort name split
        if name.strip():
            parts = name.strip().split()
            user.first_name = parts[0]
            if len(parts) > 1:
                user.last_name = " ".join(parts[1:])

        user.save(update_fields=[
            "is_staff",
            "is_superuser",
            "first_name",
            "last_name",
        ])
    except (OperationalError, ProgrammingError):
        # Database isn't ready yet (e.g., during first migrate)
        return
