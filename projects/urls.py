from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>', views.project_details, name="project_details"),
    path('unit/<slug:slug>', views.unit_details, name="unit_details"),
]