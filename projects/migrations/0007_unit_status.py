# Generated by Django 2.2.2 on 2019-06-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='status',
            field=models.CharField(default='in construction', max_length=20),
            preserve_default=False,
        ),
    ]
