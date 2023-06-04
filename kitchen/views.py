from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.models import Dish, DishType, Cook


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


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type/dish_type_list.html"
    paginate_by = 5


class DishTypeDetailView(generic.DetailView):
    model = DishType
    paginate_by = 5
    template_name = "kitchen/dish_type/dish_type_detail.html"


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
