# Generated by Django 3.0.7 on 2020-06-26 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0008_auto_20200626_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='circle_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='route',
            name='interval',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='route',
            name='time_end',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='route',
            name='time_start',
            field=models.TimeField(),
        ),
    ]
