from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import Ingredients, DishType, Dish


class ModelTest(TestCase):
    def test_ingredients_str(self):
        ingredients = Ingredients.objects.create(
            name="Test name", ingredient_cost=37
        )

        self.assertEqual(
            str(ingredients), ingredients.name
        )

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="test",
            password="Test 12345",
            first_name="test first",
            last_name="test last",
        )

        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="Test name"
        )
        self.assertEqual(str(dish_type), dish_type.name)

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="Test name"
        )
        dish = Dish.objects.create(
            name="test name",
            descriptions="Test description",
            dish_type=dish_type
        )
        self.assertEqual(str(dish), dish.name)

    def test_cook_year_of_experience(self):
        cook = get_user_model().objects.create_user(
            username="test username",
            password="Test 12345",
            year_of_experience=20,
        )
        self.assertEqual(cook.year_of_experience, 20)
        self.assertEqual(cook.username, "test username")
        self.assertTrue(cook.check_password("Test 12345"))
