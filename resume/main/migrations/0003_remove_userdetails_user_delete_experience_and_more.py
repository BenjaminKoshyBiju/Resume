# Generated by Django 4.2.2 on 2023-08-04 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_education_user_experience_user_projects_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='user',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
    ]
