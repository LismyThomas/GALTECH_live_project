# Generated by Django 4.2.7 on 2023-12-08 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_remove_courses_news_slug_courses_new_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='new_slug',
        ),
    ]
