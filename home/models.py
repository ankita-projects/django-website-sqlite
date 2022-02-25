
from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations
# python manage.py makemigrations
# python manage.py migrate     

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122, default='SOME STRING')
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
      return self.name

