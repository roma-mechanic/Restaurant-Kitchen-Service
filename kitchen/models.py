from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


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
    year_of_experience = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("kitchen:cook_detail", kwargs={"pk": self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    descriptions = models.TextField()
    dish_cost = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dish")
    ingredients = models.ManyToManyField(Ingredients, related_name="dish")

    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"
        ordering = ["dish_type", "name"]

    def __str__(self):
        return self.name

    # def dish_cost(self):
    #     return sum(cost for cost in self.ingredients.ingredient_cost())
