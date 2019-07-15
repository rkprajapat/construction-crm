from django.db import models
from datetime import date

from projects.models import Unit

status_choices = [
    ('Open', 'Open'),
    ('Closed', 'Closed')
]

class Demand(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=False, related_name='demand')
    status = models.CharField(max_length=20, choices=status_choices, blank=False)
    description = models.CharField(max_length=2000, blank=False)
    demand_date = models.DateField(verbose_name="Demand Date", auto_now_add=True)
    demand_letter = models.FileField(verbose_name="Demand Letter", blank=False)
    receipt = models.FileField(blank=True)

    @property
    def open_duration(self):
        if self.status == 'Open':
            return (date.today() - self.demand_date).days

    def __str__(self):
        return ' - '.join(str(x) for x in [self.unit, self.demand_date])
