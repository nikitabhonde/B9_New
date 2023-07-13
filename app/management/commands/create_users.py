from django.contrib.auth.models import User 
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates number')
    

    def handle(self, *args, **kwrgs):
        total = kwrgs['total']
        for i in range(total):
            User.objects.create_user(username=get_random_string(5), email='', password='Python@123')
        


"""NOTE : I create 3 custom commands 
                                        1)my_custom_commands.py 
                                        2)what_time_is_it.py 
                                        3)create_user.py    
To see all this commands -- run this on cmd -- python manage.py help
Then you found table - [app]
                        create_users
                        my_custom_command
                        what_time_is_it"""
    