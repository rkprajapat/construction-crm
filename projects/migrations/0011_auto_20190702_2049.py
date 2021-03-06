# Generated by Django 2.2.3 on 2019-07-02 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20190629_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unit',
            name='slug',
            field=models.SlugField(default='slug', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mdm.ProjectStatus'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mdm.UnitStatus'),
        ),
    ]
