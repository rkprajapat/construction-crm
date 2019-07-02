# Generated by Django 2.2.2 on 2019-06-29 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20190629_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='zip_code',
            field=models.PositiveSmallIntegerField(verbose_name='ZIP/Postal Code'),
        ),
        migrations.CreateModel(
            name='Tower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
    ]