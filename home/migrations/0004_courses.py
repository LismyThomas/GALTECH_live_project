# Generated by Django 4.2.7 on 2023-12-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_usersprofile_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=250)),
                ('course_fee', models.CharField(max_length=50)),
                ('course_description', models.TextField(blank=True, null=True)),
                ('course_type', models.BooleanField(choices=[(True, 'Paid'), (False, 'Unpaid')], default=False)),
                ('course_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]