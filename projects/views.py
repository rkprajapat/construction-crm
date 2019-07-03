from django.shortcuts import render, get_object_or_404

from .models import Project, Unit

def project_details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project/project_details.html', {'project':project})

def unit_details(request, slug):
    unit = get_object_or_404(Unit, slug=slug)
    return render(request, 'project/unit_details.html', {'unit':unit})
