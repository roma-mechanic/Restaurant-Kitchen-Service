from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class TestAdmin(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="admin123"
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="pass67890",
            year_of_experience=5,
        )

    def test_cook_year_of_experience_listed(self):
        url = reverse("admin:kitchen_cook_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.cook.year_of_experience)

    def test_cook_detail_year_of_experience(self):
        url = reverse("admin:kitchen_cook_change", args=[self.cook.id])
        res = self.client.get(url)

        self.assertContains(res, self.cook.year_of_experience)
