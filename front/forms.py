from django import forms

from .models import AirportModel, RouteModel

class FindNthNodeForm(forms.Form):
    starting = forms.ModelChoiceField(queryset=AirportModel.objects.all())
    direction = forms.ChoiceField(choices=RouteModel.POSiTION_CHOICES)
    n = forms.IntegerField()


class ShortPathForm(forms.Form):
    starting = forms.ModelChoiceField(queryset=AirportModel.objects.all())
    end = forms.ModelChoiceField(queryset=AirportModel.objects.all())