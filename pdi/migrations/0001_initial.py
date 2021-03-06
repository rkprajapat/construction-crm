# Generated by Django 2.2.3 on 2019-07-09 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PDICategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SNAG',
            fields=[
                ('snag_no', models.AutoField(primary_key=True, serialize=False)),
                ('visit_datetime', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Resolved', 'Resolved'), ('Deffered', 'Deffered')], default='Open', help_text="Deffered means can't be addressed", max_length=20)),
                ('description', models.CharField(max_length=5000)),
                ('images', models.ImageField(upload_to='')),
                ('acknowledgement', models.CharField(choices=[('Open', 'Open'), ('Accepted', 'Accepted'), ('Pending', 'Pending')], default='Open', help_text='Customer feedback', max_length=20)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pdi.PDICategory')),
            ],
        ),
    ]
