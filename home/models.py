# home/models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    objects = models.Manager()

    def __str__(self):
        return self.name
