from django.db import models

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
    documents = models.FileField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.title
