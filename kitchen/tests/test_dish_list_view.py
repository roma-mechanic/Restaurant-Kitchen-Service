from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import Dish, DishType


class TestDishListView(TestCase):
    def setUp(self):
        self.client = Client()
        test_dish_type = DishType.objects.create(name="test dish type")
        self.user = get_user_model().objects.create_user(
            username="test_name", password="test_password"
        )
        Dish.objects.create(
            name="super_dish",
            descriptions="test description",
            dish_type=test_dish_type,
        )
        Dish.objects.create(
            name="mega_dish",
            descriptions="test description",
            dish_type=test_dish_type,
        )
        Dish.objects.create(
            name="uber_dish",
            descriptions="test description",
            dish_type=test_dish_type,
        )

    def test_search_field(self):
        self.client.force_login(self.user)
        get_value = "Piz"
        url = reverse("kitchen:dish-list") + f"?name={get_value}"

        response = self.client.get(url)
        dish_query = Dish.objects.filter(name__icontains=get_value)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_list"]), list(dish_query))

    def test_login_required(self):
        url = reverse("kitchen:dish-list")
        response = self.client.get(url)

        self.assertNotEquals(response.status_code, 200)
