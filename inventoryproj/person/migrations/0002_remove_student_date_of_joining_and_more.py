# Generated by Django 4.0.4 on 2022-06-01 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_of_joining',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='date_of_joining',
        ),
    ]
