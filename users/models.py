from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from phonenumber_field.modelfields import PhoneNumberField


class Role(models.Model):
    role = models.CharField(max_length=254, blank=False)
    description = models.CharField(max_length=1024, blank=True)

    def __str__(self):
        return self.role


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    slug = models.SlugField(unique=True)
    username = models.CharField(max_length=20, null=True)
    full_name = models.CharField(verbose_name='Full Name', max_length=254, blank=False)
    address = models.CharField(max_length=2048, default=None, blank=True, null=True)
    roles = models.ManyToManyField(Role, blank=True)
    primary_phone_number = PhoneNumberField(verbose_name='Primary Phone', blank=False, help_text='Enter valid phone number with country/area code')
    secondary_phone_number = PhoneNumberField(verbose_name='Secondary Phone', blank=True, null=True, help_text='Enter valid phone number with country/area code')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.email)
        super(CustomUser, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("users:account", kwargs={"slug": self.slug})

    @property
    def is_customer(self):
        return self.roles.filter(role='Customer').exists()

    @property
    def is_project_admin(self):
        return self.roles.filter(role='Project Admin').exists()
    
    def __str__(self):
        return "{0} <{1}>".format(self.full_name, self.email.lower())

