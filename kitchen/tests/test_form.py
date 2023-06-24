from django.test import TestCase

from kitchen.forms import CookCreationForm


class TestCookCreationForm(TestCase):
    def test_cook_form_intro(self):
        form_data = {
            "username": "cheefcook",
            "year_of_experience": 7,
            "first_name": "first",
            "last_name": "last",
            "password1": "admin-1234",
            "password2": "admin-1234",
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form_data, form.cleaned_data)
