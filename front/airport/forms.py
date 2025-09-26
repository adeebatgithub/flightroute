from django import forms

from front.models import AirportModel


class AirportForm(forms.ModelForm):
    class Meta:
        model = AirportModel
        fields = '__all__'