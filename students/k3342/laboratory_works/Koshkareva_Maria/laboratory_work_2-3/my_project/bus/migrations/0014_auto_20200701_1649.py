# Generated by Django 3.0.7 on 2020-07-01 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0013_auto_20200701_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='work_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 16, 49, 46, 117939)),
        ),
        migrations.AddField(
            model_name='schedule',
            name='work_start',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 16, 49, 46, 117939)),
        ),
    ]