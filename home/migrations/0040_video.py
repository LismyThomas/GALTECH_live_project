# Generated by Django 4.2.7 on 2023-12-12 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_courses_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=50)),
                ('thumbnail', models.CharField(help_text='Thumbnail location name', max_length=250)),
                ('video_upload_url', models.CharField(help_text='Video url', max_length=250)),
                ('note', models.TextField(blank=True, null=True)),
                ('video_file', models.CharField(help_text='Video location name', max_length=250)),
                ('duration', models.CharField(max_length=20)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.lessons')),
            ],
        ),
    ]