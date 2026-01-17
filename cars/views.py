from django.shortcuts import render


def cars_view(request):
    return render(request, "cars.html", {"cars": {"model": "Polo 1.6"}})
