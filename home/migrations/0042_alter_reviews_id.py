# Generated by Django 4.2.7 on 2023-12-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
