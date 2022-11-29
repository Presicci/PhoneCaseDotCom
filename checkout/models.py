# home/models.py
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/')

