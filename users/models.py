from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class Role(models.Model):
  '''
  The Role entries are managed by the system,
  automatically created via a Django data migration.
  '''
  CUSTOMER = 1
  CRM = 2
  DESIGN = 3
  CONSTRUCTION = 4
  ADMIN = 5
  ROLE_CHOICES = (
      (CUSTOMER, 'CUSTOMER'),
      (CRM, 'CRM'),
      (DESIGN, 'DESIGN'),
      (CONSTRUCTION, 'CONSTRUCTION'),
      (ADMIN, 'ADMIN'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True, default=1,)

  def __str__(self):
      return self.get_id_display()




class CustomUser(AbstractUser):
    address = models.CharField(max_length=2048,default=None, blank=True, null=True)
    roles = models.ManyToManyField(Role)
    primary_phone_number = PhoneNumberField(verbose_name='Primary Phone', blank=False, help_text='Enter valid phone number with country/area code')
    secondary_phone_number = PhoneNumberField(verbose_name='Secondary Phone', blank=True, null=True, help_text='Enter valid phone number with country/area code')

    def __str__(self):
        return self.email