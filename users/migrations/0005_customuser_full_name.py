# Generated by Django 2.2 on 2019-06-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190628_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(default='admin', max_length=254, verbose_name='Full Name'),
            preserve_default=False,
        ),
    ]
