from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    url = models.CharField(max_length=100)