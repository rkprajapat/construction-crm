from django.db import models
from django_countries.fields import CountryField

class Project(models.Model):
    name = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length=50, blank=False)
    address1 = models.CharField(max_length=254, blank=False)
    address2 = models.CharField(max_length=254, blank=True)
    city = models.CharField(max_length=50, blank=False)
    zip_code = models.CharField('ZIP/Postal Code', max_length=12)
    country = CountryField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name