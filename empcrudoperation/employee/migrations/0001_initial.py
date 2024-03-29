# Generated by Django 4.0.4 on 2022-06-08 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
