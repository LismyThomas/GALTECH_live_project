# Generated by Django 4.2.7 on 2023-12-04 03:42

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_courses_course_img_courses_c_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='c_images',
        ),
        migrations.AddField(
            model_name='courses',
            name='course_img',
            field=models.ImageField(blank=True, default='course/', null=True, upload_to=home.models.unique_name),
        ),
    ]
