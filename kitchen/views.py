from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import SearchForm, CooksSearchForm, CookCreationForm
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


"""cooks"""


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5
    template_name = "kitchen/cooks/cooks_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["cooks_search_form"] = CooksSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Cook.objects.all()
        form = CooksSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["username"])
        return queryset


class CookDetailView(generic.DetailView):
    model = Cook
    # queryset = Cook.objects.all().prefetch_related("dish__cooks")
    template_name = "kitchen/cooks/cook_detail.html"


class CookCreateView(generic.CreateView):
    model = Cook
    # fields = "__all__"
    form_class = CookCreationForm
    template_name = "kitchen/create-update_form.html"
    success_url = reverse_lazy("kitchen:cooks-list")


class CookUpdateView(generic.UpdateView):
    model = Cook
    fields = "__all__"
    template_name = "kitchen/create-update_form.html"
    success_url = reverse_lazy("kitchen:cooks-list")


class CookDeleteView(generic.DeleteView):
    model = Cook
    template_name = "kitchen/cooks/cook_confirm_delete.html"
    success_url = reverse_lazy("kitchen:cooks-list")


"""dishes"""


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5
    template_name = "kitchen/dishes/dishes_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["dish_search_form"] = SearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Dish.objects.all()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    template_name = "kitchen/create-update_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "kitchen/dishes/dish-details.html"


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    template_name = "kitchen/create-update_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishDeleteView(generic.DeleteView):
    model = Dish
    template_name = "kitchen/dishes/dish_confirm_delete.html"
    success_url = "kitchen:dish-type-list"
