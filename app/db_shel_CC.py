# 118 (custom Commands)
# exec(open(r'E:\djangoLibPrroject\B9__Library\app\db_shel_CC.py').read())

from django.contrib.auth.models import User


# print(User.objects.all())   # Gives the all Users that we created 

# User.objects.create(username="Krishna", password="Python@123")       # It create the user bt Password is visible in database

# User.objects.create_user(username="Shaym", password="Python@123")    # It create the user & Password is encrypted (****) 

# from django.utils.crypto import get_random_string                    # get_random_string gives you a any random_string (a-z, A-Z 0-9) 
# print(get_random_string(5))