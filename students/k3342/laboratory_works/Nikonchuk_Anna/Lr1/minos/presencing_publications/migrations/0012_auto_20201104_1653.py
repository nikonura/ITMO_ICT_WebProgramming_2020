# Generated by Django 3.1.2 on 2020-11-04 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presencing_publications', '0011_auto_20201104_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
    ]