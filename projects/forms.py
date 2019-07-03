from django import forms
from searchableselect.widgets import SearchableSelect
from .models import Unit

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        exclude = ()
        widgets = {
            'owner': SearchableSelect(model='users.CustomUser', search_field='full_name', limit=10, many=True, attrs={'placeholder':'Search name'})
        }