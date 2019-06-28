# Generated by Django 2.2 on 2019-06-28 08:31

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190628_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='primary_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Primary Phone', max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='secondary_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Secondary Phone', max_length=128, region=None),
        ),
    ]