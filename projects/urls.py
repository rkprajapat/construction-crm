from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>', views.project_details, name="project_details"),
]