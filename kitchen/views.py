from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
    return render(request, "kitchen/index.html", context= context)
