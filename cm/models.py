from __future__ import unicode_literals

from django.db import models
# Create your models here.]


class Manufacturer(models.Model):
    name = models.CharField(max_length=32)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=5, max_digits=16)
    description = models.TextField()
    release_date = models.DateField()
    manufacturer = models.ForeignKey(Manufacturer)





