# Generated by Django 3.0.3 on 2020-05-07 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default='1999-19-09'),
        ),
    ]
