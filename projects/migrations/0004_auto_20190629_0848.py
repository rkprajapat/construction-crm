# Generated by Django 2.2.2 on 2019-06-29 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20190629_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='address1',
            field=models.CharField(max_length=254, verbose_name='Address Line 1'),
        ),
        migrations.AlterField(
            model_name='project',
            name='address2',
            field=models.CharField(blank=True, max_length=254, verbose_name='Address Line 2'),
        ),
    ]
