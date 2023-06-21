from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import Cook


class TestCookListView(TestCase):
    def setUp(self):
        self.cook_1 = get_user_model().objects.create_user(
            username="Bob", password="pass67890", year_of_experience="12"
        )
        self.cook_2 = get_user_model().objects.create_user(
            username="Alice", password="pass67890", year_of_experience="4"
        )
        self.cook_3 = get_user_model().objects.create_user(
            username="Marline", password="pass67890", year_of_experience="9"
        )

        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="test_user", password="test_password"
        )

    def test_search_field(self):
        self.client.force_login(self.user)
        get_value = "Mar"
        url = reverse("kitchen:cooks-list") + f"?username={get_value}"
        response = self.client.get(url)
        driver_query = Cook.objects.filter(username__icontains=get_value)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["cook_list"]),
                         list(driver_query))

    def test_login_required(self):
        url = reverse("kitchen:cooks-list")
        response = self.client.get(url)

        self.assertNotEquals(response.status_code, 200)
