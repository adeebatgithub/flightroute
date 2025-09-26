from datetime import timedelta

from django import forms

from front.models import RouteModel


class RouteForm(forms.ModelForm):
    class Meta:
        model = RouteModel
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        starting = cleaned_data.get('starting')
        position = cleaned_data.get('position')
        ending = cleaned_data.get('ending')

        if not self.instance.pk:
            if starting and ending and starting == ending:
                raise forms.ValidationError("You can't start and end the same route.")

            if RouteModel.objects.filter(starting=starting, position=position).exists():
                raise forms.ValidationError("route exists in this position.")

            if RouteModel.objects.filter(starting=starting, ending=ending).exists():
                raise forms.ValidationError("route already exists.")

        return cleaned_data
