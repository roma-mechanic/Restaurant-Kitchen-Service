from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from kitchen.models import Dish, DishType, Cook


@login_required
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


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type/dish_type_list.html"
    paginate_by = 5
