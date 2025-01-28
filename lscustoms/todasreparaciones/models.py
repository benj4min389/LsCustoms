from django.db import models

# Create your models here.
class Miembro(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    email = models.EmailField()
    password = models.CharField(max_length=16)
    type_user = models.CharField(max_length=50)