from django.contrib import admin

from .models import ProjectStatus, UnitStatus

class MDMAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProjectStatus, MDMAdmin)
admin.site.register(UnitStatus, MDMAdmin)
