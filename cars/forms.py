from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def clean_value(self):
        value = self.cleaned_data.get("value")

        if value < 20000:
            self.add_error("value", "We can't accept cars cheaper than U$ 20.000.")

        return value

    def clean_manufacture_year(self):
        value = self.cleaned_data.get("manufacture_year")

        if value < 1960:
            self.add_error("manufacture_year", "We can't accept cars older than 1960.")

        return value
