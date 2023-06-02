from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    year_of_experience = models.IntegerField
