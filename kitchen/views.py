from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import SearchForm
from kitchen.models import Dish, DishType, Cook, Ingredients


# @login_required
def index(request):
    num_dish = Dish.objects.count()
    num_type_dish = DishType.objects.count()
    num_cooks = Cook.objects.count()

    context = {
        "num_dish": num_dish,
        "num_type_dish": num_type_dish,
        "num_cooks": num_cooks
    }
    return render(request, "kitchen/index.html", context=context)


"""Dish Types"""


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type/dish_type_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["dish_type_search_form"] = SearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishTypeDetailView(generic.DetailView):
    model = DishType
    paginate_by = 5
    template_name = "kitchen/dish_type/dish_type_detail.html"


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/create-update_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/create-update_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    template_name = "kitchen/dish_type/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


"""ingredients"""


class IngredientListView(generic.ListView):
    model = Ingredients
    template_name = "kitchen/ingredients/ingredients_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["ingredients_search_form"] = SearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Ingredients.objects.all()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class IngredientCreateView(generic.CreateView):
    model = Ingredients
    fields = "__all__"
    template_name = "kitchen/create-update_form.html"
    success_url = reverse_lazy("kitchen:ingredients-list")


class IngredientUpdateView(generic.UpdateView):
    model = Ingredients
    fields = "__all__"
    template_name = "kitchen/create-update_form.html"
    success_url = reverse_lazy("kitchen:ingredients-list")


class IngredientDeleteView(generic.DeleteView):
    model = Ingredients
    template_name = "kitchen/ingredients/ingredients_confirm_delete.html"
    success_url = reverse_lazy("kitchen:ingredients-list")
