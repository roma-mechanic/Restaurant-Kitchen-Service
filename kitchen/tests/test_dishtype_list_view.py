from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import DishType


class TestDishTypeListView(TestCase):
    def setUp(self):
        self.client = Client()
        DishType.objects.create(name="super_dish_type")
        DishType.objects.create(name="mega_dish_type")
        DishType.objects.create(name="uber_dish_type")
        self.user = get_user_model().objects.create_user(
            username="test_name", password="test_password"
        )

    def test_search_field(self):
        self.client.force_login(self.user)
        get_value = "Bor"
        url = reverse("kitchen:dish-type-list") + f"?name={get_value}"

        response = self.client.get(url)
        dish_type_query = DishType.objects.filter(name__icontains=get_value)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dishtype_list"]), list(dish_type_query))

    def test_login_required(self):
        url = reverse("kitchen:dish-type-list")
        response = self.client.get(url)

        self.assertNotEquals(response.status_code, 200)
