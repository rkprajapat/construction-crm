from django.db import models
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

    def __str__(self):
        return self.name


class Tower(models.Model):
    name = models.CharField(max_length=20, blank=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return ' '.join([self.project.name, '-', self.name])


class Unit(models.Model):
    unit = models.PositiveSmallIntegerField(blank=False)
    project_tower = models.ForeignKey(Tower, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return ' '.join([self.project_tower.project.name, self.project_tower.name, str(self.unit)])