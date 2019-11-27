from django import forms
from .models import WeatherData


class WeatherSubscribeForm(forms.ModelForm):
    class Meta:
        model = WeatherData
        fields = ('city',)

    def save(self, commit=False):
        pass
