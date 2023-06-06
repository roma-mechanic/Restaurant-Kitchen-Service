from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Ingredients, Cook


class SearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class CooksSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


# class CookCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = get_user_model()
#         fields = UserCreationForm.Meta.fields + ("year_of_experience",)


class IngredientsForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredients.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Ingredients
        fields = "__all__"


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (

            "first_name",
            "last_name",
            "year_of_experience",
        )
