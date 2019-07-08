from django import forms

from .models import Demand

class DemandForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Demand
        exclude = ()