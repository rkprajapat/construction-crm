# Generated by Django 2.2.3 on 2019-07-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demands', '0004_auto_20190708_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='demand_letter',
            field=models.FileField(upload_to='', verbose_name='Demand Letter'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='receipt',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
