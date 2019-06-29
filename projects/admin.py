from django.contrib import admin

from .models import Project, Tower, Unit

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Tower, ProjectAdmin)
admin.site.register(Unit, ProjectAdmin)