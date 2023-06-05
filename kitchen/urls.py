from django.urls import path

from .views import (
    index,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("dish_type/",
         DishTypeListView.as_view(),
         name="dish-type-list"),
    path("dish_type/<int:pk>/detail/",
         DishTypeDetailView.as_view(),
         name="dish-type-detail"),
    path("dish_type/create/",
         DishTypeCreateView.as_view(),
         name="dish-type-create"),
    path("dish_type/<int:pk>/update/",
         DishTypeUpdateView.as_view(),
         name="dish-type-update"),
    path("dish_type/<int:pk>/delete/",
         DishTypeDeleteView.as_view(),
         name="dish-type-delete"),
    path("ingredients/",
         IngredientListView.as_view(),
         name="ingredients-list"),
    path("ingredients/create/",
         IngredientCreateView.as_view(),
         name="ingredients-create"),
    path("ingredients/<int:pk>/update/",
         IngredientUpdateView.as_view(),
         name="ingredients-update"),
    path("ingredients/<int:pk>/delete/",
         IngredientDeleteView.as_view(),
         name="ingredients-delete"),
]

app_name = "kitchen"
