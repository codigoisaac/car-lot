from django.contrib import admin
from cars.models import Car, Brand, CarInventory


class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "brand", "model_year", "value", "photo")
    search_fields = ("model", "brand", "model_year")


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ("cars_count", "cars_value", "created_at")


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(CarInventory, InventoryAdmin)
