from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create multiple users'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of users to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        for i in range(count):
            username = f'user{i}'
            password = 'password123' 
            email = f'user{i}@example.com'  
            User.objects.create_user(username=username, password=password, email=email)
            self.stdout.write(self.style.SUCCESS(f'Successfully created user: {username}'))
