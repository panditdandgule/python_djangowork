# Generated by Django 4.0.4 on 2022-06-08 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
