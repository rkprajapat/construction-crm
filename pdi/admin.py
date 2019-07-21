from django.contrib import admin

from .models import SNAG, PDICategory
from .forms import SNAGForm

class PDICategoryAdmin(admin.ModelAdmin):
    pass

class SNAGAdmin(admin.ModelAdmin):
    form = SNAGForm
    list_display = ['snag_no', 'snag_datetime', 'category', 'status', 'acknowledgement']

    class Meta:
        model = SNAG


admin.site.register(SNAG, SNAGAdmin)
admin.site.register(PDICategory, PDICategoryAdmin)
