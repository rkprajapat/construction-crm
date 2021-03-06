# Generated by Django 2.2 on 2019-06-28 05:44

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'CUSTOMER'), (2, 'CRM'), (3, 'DESIGN'), (4, 'CONSTRUCTION'), (5, 'admin')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='primary_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='customuser',
            name='secondary_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='customuser',
            name='roles',
            field=models.ManyToManyField(to='users.Role'),
        ),
    ]
