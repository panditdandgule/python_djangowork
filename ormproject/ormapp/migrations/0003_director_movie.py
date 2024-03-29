# Generated by Django 4.0.4 on 2022-04-29 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0002_teacher_student_teacher_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=150)),
                ('release_year', models.IntegerField()),
                ('director', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='ormapp.director')),
            ],
        ),
    ]
