from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField

class Project(models.Model):
    name = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length=50, blank=False)
    address1 = models.CharField('Address Line 1', max_length=254, blank=False)
    address2 = models.CharField('Address Line 2', max_length=254, blank=True)
    city = models.CharField(max_length=50, blank=False)
    zip_code = models.PositiveSmallIntegerField('ZIP/Postal Code')
    country = CountryField()
    image = models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse('project_details', args=[str(self.id)])

    def __str__(self):
        return self.name


class Tower(models.Model):
    name = models.CharField(max_length=20, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        if self.name:
            return ' '.join([self.project.name, '-', self.name])
        else:
            return self.project.name


class Unit(models.Model):
    unit = models.PositiveSmallIntegerField(blank=False)
    project_tower = models.ForeignKey(Tower, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, blank=False)

    class Meta:
        ordering = ['project_tower', 'unit']

    def get_absolute_url(self):
        return reverse('unit_details', args=[str(self.id)])

    def __str__(self):
        return ' '.join([self.project_tower.project.name, self.project_tower.name, str(self.unit)])