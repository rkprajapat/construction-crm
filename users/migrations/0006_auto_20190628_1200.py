# Generated by Django 2.2 on 2019-06-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'CUSTOMER'), (2, 'CRM'), (3, 'DESIGN'), (4, 'CONSTRUCTION'), (5, 'ADMIN')], primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='roles',
            field=models.ManyToManyField(default=1, null=True, to='users.Roles'),
        ),
    ]
