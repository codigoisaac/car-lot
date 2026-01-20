from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView


class CarsView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        search = self.request.GET.get("search")

        if search:
            cars = (
                super().get_queryset().filter(model__contains=search).order_by("model")
            )
        else:
            cars = super().get_queryset().order_by("model")

        return cars


class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()

        return render(request, "new_car.html", {"new_car_form": new_car_form})

    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)

        if new_car_form.is_valid():
            new_car_form.save()

            return redirect("cars")

        return render(request, "new_car.html", {"new_car_form": new_car_form})
