from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import Ingredients


class TestIngredientsListView(TestCase):
    def setUp(self):
        self.client = Client()
        Ingredients.objects.create(name="super_ingredient", ingredient_cost=47)
        Ingredients.objects.create(name="mega_ingredient", ingredient_cost=47)
        Ingredients.objects.create(name="uber_ingredient", ingredient_cost=47)
        self.user = get_user_model().objects.create_user(
            username="test_name", password="test_password"
        )

    def test_search_field(self):
        self.client.force_login(self.user)
        get_value = "but"
        url = reverse("kitchen:ingredients-list") + f"?name={get_value}"

        response = self.client.get(url)
        ingredient_query = Ingredients.objects.filter(name__icontains=get_value)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["ingredients_list"]), list(ingredient_query))

    def test_login_required(self):
        url = reverse("kitchen:ingredients-list")
        response = self.client.get(url)

        self.assertNotEquals(response.status_code, 200)