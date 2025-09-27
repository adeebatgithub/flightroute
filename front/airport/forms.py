from django import forms

from front.models import AirportModel


class AirportForm(forms.ModelForm):
    """ModelForm for Airport - auto-generates fields from model"""

    class Meta:
        model = AirportModel
        fields = '__all__'  # Include all model fields in the form