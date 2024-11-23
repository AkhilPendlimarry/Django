from django.db import models

# Create your models here.
class customer(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=100)
    customer_phone = models.IntegerField()
    customer_address = models.CharField(max_length=200)
    customer_city = models.CharField(max_length=100)