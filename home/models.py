# home/models.py
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
