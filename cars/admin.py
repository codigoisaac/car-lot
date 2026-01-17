from django.contrib import admin
from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "brand", "model_year", "value")
    search_fields = ("model", "brand", "model_year")


admin.site.register(Car, CarAdmin)
