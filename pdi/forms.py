from django import forms

from .models import SNAG

class SNAGForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))

    class Meta:
        model = SNAG
        exclude = ()