from django import forms

from .models import Document

class DocumentForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    documents = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}), required=True)


    class Meta:
        model = Document
        exclude = ()