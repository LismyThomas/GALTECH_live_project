# Generated by Django 4.2.7 on 2023-12-06 05:24

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_remove_courses_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='news_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='course_name', unique=True),
        ),
    ]