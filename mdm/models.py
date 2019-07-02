from django.db import models
from django.urls import reverse

class ProjectStatus(models.Model):
    status = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name = 'Project Status'
        verbose_name_plural = 'Project Status'

    def __str__(self):
        return self.status

class UnitStatus(models.Model):
    status = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name = 'Unit Status'
        verbose_name_plural = 'Unit Status'

    def __str__(self):
        return self.status