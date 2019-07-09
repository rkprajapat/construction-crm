from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import DocumentForm

class FileFieldView(FormView):
    form_class = DocumentForm
    # template_name = 'upload.html'  # Replace with your template.
    # success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('documents')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
