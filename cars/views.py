from django.shortcuts import render
from cars.models import Car


def cars_view(request):
    search = request.GET.get("search")

    if search:
        cars = Car.objects.filter(model__contains=search).order_by("model")
    else:
        cars = Car.objects.all().order_by("model")

    return render(request, "cars.html", {"cars": cars})
