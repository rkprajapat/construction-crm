from django.db import models

from projects.models import Unit, Tower, Project

class Library(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'


class Document(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=2000)
    file = models.FileField(blank=False)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, blank=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name="docs")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True, related_name="docs")
    published = models.BooleanField(help_text="Once published, document is visible to customers.", default=False)

    def __str__(self):
        return self.title
