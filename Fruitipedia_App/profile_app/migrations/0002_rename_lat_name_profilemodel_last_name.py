# Generated by Django 4.2.5 on 2023-09-11 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilemodel',
            old_name='lat_name',
            new_name='last_name',
        ),
    ]
