# Generated by Django 4.2.7 on 2023-12-08 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_alter_courses_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='slug',
        ),
    ]
