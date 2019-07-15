from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Project, Unit
from libraries.models import Library, Document

def project_details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project/project_details.html', {'project':project})

def unit_details(request, slug):
    unit = get_object_or_404(Unit, slug=slug)
    docs = Document.objects.filter(published=True).filter(Q(unit=unit) | Q(project=unit.project))
    return render(request, 'project/unit_details.html', {'unit':unit, 'docs':docs})
