# Generated by Django 4.2.7 on 2023-12-08 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_courses_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='slug',
        ),
    ]
