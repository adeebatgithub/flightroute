from django import forms

from front.models import RouteModel


class RouteForm(forms.ModelForm):
    """ModelForm for Route with custom validation"""

    class Meta:
        model = RouteModel
        fields = '__all__'

    def clean(self):
        """Custom validation to prevent duplicate routes and invalid combinations"""
        cleaned_data = super().clean()
        starting = cleaned_data.get('starting')
        position = cleaned_data.get('position')
        ending = cleaned_data.get('ending')

        # Only validate on new records (not updates)
        if not self.instance.pk:
            # Prevent same starting and ending airport
            if starting and ending and starting == ending:
                raise forms.ValidationError("You can't start and end the same route.")

            # Prevent duplicate position for same starting airport
            if RouteModel.objects.filter(starting=starting, position=position).exists():
                raise forms.ValidationError("route exists in this position.")

            # Prevent duplicate routes
            if RouteModel.objects.filter(starting=starting, ending=ending).exists():
                raise forms.ValidationError("route already exists.")

        return cleaned_data
