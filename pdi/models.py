from django.db import models

from projects.models import Unit

snag_status_choices = [
    ('Open', 'Open'),
    ('Resolved', 'Resolved'),
    ('Deffered', 'Deffered')
]

snag_acknowledgement_choices = [
    ('Open', 'Open'),
    ('Accepted', 'Accepted'),
    ('Pending', 'Pending')
]

class PDICategory(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'PDI Category'
        verbose_name_plural = 'PDI Categories'


class SNAG(models.Model):
    snag_no = models.CharField(editable=False, max_length=50, null=True)
    snag_datetime = models.DateTimeField(auto_now_add=True, editable=False)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=False, related_name='snags')
    category = models.ForeignKey(PDICategory, on_delete=models.SET_NULL, null=True, blank=False)
    status = models.CharField(max_length=20, blank=False, choices=snag_status_choices, help_text='Deffered means can\'t be addressed', default=snag_status_choices[0][0])
    description = models.CharField(max_length=5000, blank=False)
    images = models.ImageField()
    acknowledgement = models.CharField(max_length=20, blank=False, choices=snag_acknowledgement_choices, default=snag_acknowledgement_choices[0][0], help_text='Customer feedback')
    
    def save(self, *args, **kwargs):
        snag_no = ''.join(str(x) for x in [self.unit.unit, self.snag_datetime.strftime("%Y%m%d"), self.unit.snags.count()+1])
        self.snag_no = snag_no
        super(SNAG, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.snag_no)



