from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ingredient_cost = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    year_of_experience = models.IntegerField


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    descriptions = models.TextField
    dish_cost = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dish")
    ingredients = models.ManyToManyField(Ingredients, related_name="dish")

    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"
        ordering = ["dish_type", "name"]

    def __str__(self):
        return self.dish_type, self.name

