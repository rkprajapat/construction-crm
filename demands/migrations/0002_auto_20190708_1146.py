# Generated by Django 2.2.3 on 2019-07-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='status',
            field=models.CharField(choices=[(1, 'Open'), (2, 'Closed')], default=1, max_length=20),
        ),
    ]