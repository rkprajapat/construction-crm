# Generated by Django 2.2.2 on 2019-06-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20190629_0918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['project_tower', 'unit']},
        ),
        migrations.AlterField(
            model_name='tower',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
