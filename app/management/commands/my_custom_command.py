# (django 118)
# (b9_env) E:\djangoLibPrroject\B9__Library>py manage.py my_custom_command       --  run this on cmd
from typing import Any, Optional
from django.contrib.auth.models import User             # To import User module
from django.core.management.base import BaseCommand     
from django.utils.crypto import get_random_string       # To generate random String
from django.utils import timezone 

class Command(BaseCommand):
    help = 'This is custom commands'
    
    def handle(self, *args: Any, **options: Any):
        print("Go to this website {https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html} for more informations")
 

"""NOTE : I create 3 custom commands 
                                        1)my_custom_commands.py 
                                        2)what_time_is_it.py 
                                        3)create_user.py    
To see all this commands -- run this on cmd -- python manage.py help
Then you found table - [app]
                        create_users
                        my_custom_command
                        what_time_is_it"""