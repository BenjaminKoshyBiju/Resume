# Generated by Django 4.2.2 on 2023-08-11 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_userdetails_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='user',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='user',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='user',
        ),
    ]
