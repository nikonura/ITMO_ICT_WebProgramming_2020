# Generated by Django 3.0.4 on 2020-04-17 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights_app', '0002_auto_20200417_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightactivities',
            name='activity',
            field=models.CharField(choices=[('0', 'arrival'), ('1', 'departure')], default='0', max_length=1),
        ),
    ]
