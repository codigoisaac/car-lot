from django import forms
from cars.models import Brand, Car


class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    manufacture_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def create(self):
        car = Car(
            model=self.cleaned_data["model"],
            brand=self.cleaned_data["brand"],
            manufacture_year=self.cleaned_data["manufacture_year"],
            model_year=self.cleaned_data["model_year"],
            plate=self.cleaned_data["plate"],
            value=self.cleaned_data["value"],
            photo=self.cleaned_data["photo"],
        )

        car.save()

        return car
