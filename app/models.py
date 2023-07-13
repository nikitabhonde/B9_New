from django.db import models
from django.utils import timezone


# If humne koi class bnaya jisko humme project mai add nhi krna hai to hum usko abstract_class 
# means (abstract = True) krte hai inside class Meta
# mostly eska use CommonMethods define krne kai liye hota hai 
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)

    class Meta:
        abstract = True 


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=200, default='Unknown')
    price = models.IntegerField()                        # IntegerField for numbers
    qty = models.CharField(max_length=100)               # CharField for Cahr/words
    publication_date = models.DateField()
    is_published = models.BooleanField(default=True)     # BooleanField for T & F (bydefault value false aste) ya ex mddhe apn true keli aahe
    is_active = models.BooleanField(default=True)
    
   

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.name