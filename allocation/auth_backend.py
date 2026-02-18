from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

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
