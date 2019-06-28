from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length=50, blank=False)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name