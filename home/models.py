# home/models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=15)
    quantity = models.IntegerField(default=100)
    image = models.ImageField(upload_to='images/')
    objects = models.Manager()
    sale = models.BooleanField(default=0)
    sale_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
