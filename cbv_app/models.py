from django.db import models

# video 118 (we create cbv_app for write code for Class Based Views)

class Employee(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    mobile = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)               # another way of string represation
    
    class Meta:
        db_table = "employee"                                            # here we use class meta to change the table name


# step 1)create class after creating class nd defining methods in it do 1)python manage.py makemigrations 2)python manage.py migrate