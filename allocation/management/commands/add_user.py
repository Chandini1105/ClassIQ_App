from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()
DEFAULT_PASSWORD = "CMRU 1"

class Command(BaseCommand):
    help = 'Add a new user with default password (CMRU 1) and @cmr.edu.in email'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name (first and last name)')
        parser.add_argument('--email', type=str, help='Email (optional, auto-generated if not provided)')

    def handle(self, *args, **options):
        name = options['name']
        email = options.get('email')

        # Auto-generate email if not provided
        if not email:
            # Convert name to email format: "John Doe" -> "johndoe@cmr.edu.in"
            email_part = name.lower().replace(' ', '').replace('-', '')
            email = f"{email_part}@cmr.edu.in"

        # Validate email ends with @cmr.edu.in
        if not email.endswith('@cmr.edu.in'):
            self.stdout.write(
                self.style.ERROR(f'Email must end with @cmr.edu.in, got: {email}')
            )
            return

        # Check if user already exists
        if User.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.ERROR(f'User with email {email} already exists!')
            )
            return

        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                first_name=name.split()[0] if len(name.split()) > 0 else name,
                last_name=' '.join(name.split()[1:]) if len(name.split()) > 1 else '',
                password=DEFAULT_PASSWORD
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f'✓ User created successfully!\n'
                    f'  Email: {email}\n'
                    f'  Password: {DEFAULT_PASSWORD}'
                )
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating user: {str(e)}'))
