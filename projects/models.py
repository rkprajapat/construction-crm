from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from django.utils.text import slugify

from mdm.models import ProjectStatus, UnitStatus
from users.models import CustomUser

class Project(models.Model):
    name = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(unique=True)
    status = models.ForeignKey(ProjectStatus, blank=False, null=True, on_delete=models.SET_NULL)
    address1 = models.CharField('Address Line 1', max_length=254, blank=False)
    address2 = models.CharField('Address Line 2', max_length=254, blank=True)
    city = models.CharField(max_length=50, blank=False)
    zip_code = models.PositiveSmallIntegerField('ZIP/Postal Code')
    country = CountryField()
    image = models.ImageField(blank=True, )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_details', args=[str(self.slug)])

    @property
    def address(self):
        return ', '.join(str(x) for x in [self.address1, self.address2, self.city, self.zip_code, self.country.name] if x)


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
    status = models.ForeignKey(UnitStatus, blank=False, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(unique=True)
    owner = models.ManyToManyField(CustomUser, blank=True)

    class Meta:
        ordering = ['project_tower', 'unit']

    def save(self, *args, **kwargs):
        self.slug = slugify('-'.join([self.project_tower.project.name, self.project_tower.name, str(self.unit)]))
        super(Unit, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('unit_details', args=[str(self.slug)])

    @property
    def address(self):
        return self.project_tower.project.address

    def __str__(self):
        return ' '.join([self.project_tower.project.name, self.project_tower.name, str(self.unit)])