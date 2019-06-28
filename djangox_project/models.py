from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    def __str__(self):
        return self.email

class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_createdby')
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='%(class)s_modifiedby', null=True, blank=True)

    class Meta:
        abstract=True # Set this model 