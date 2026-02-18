from django.core.management.base import BaseCommand

from allocation.utils.default_user import ensure_default_user


class Command(BaseCommand):
    help = "Ensure the default login user exists (env-based)"

    def handle(self, *args, **options):
        ensure_default_user()
        self.stdout.write(self.style.SUCCESS("Default user ensure completed."))
