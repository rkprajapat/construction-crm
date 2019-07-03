from django.contrib import admin

from .models import Project, Tower, Unit
from .forms import UnitForm

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    exclude = ('slug',)
    # pass

class TowerAdmin(admin.ModelAdmin):
    list_display = ['name', 'project']
    exclude = ('slug',)
    # pass

class UnitAdmin(admin.ModelAdmin):
    form = UnitForm
    list_display = ['unit','project_tower', 'status']
    exclude = ('slug',)
    
    # pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Tower, TowerAdmin)
admin.site.register(Unit, UnitAdmin)