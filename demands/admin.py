from django.contrib import admin

from .models import Demand
from .forms import DemandForm

class DemandAdmin(admin.ModelAdmin):
    form = DemandForm
    list_display = ('pk', 'unit', 'demand_date', 'open_duration')
    search_fields = ('unit', )

admin.site.register(Demand, DemandAdmin)
