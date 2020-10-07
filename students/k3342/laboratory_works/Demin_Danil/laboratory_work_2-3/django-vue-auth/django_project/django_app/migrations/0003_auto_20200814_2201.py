# Generated by Django 3.0.8 on 2020-08-14 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_auto_20200705_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='breed',
            name='avg_productivity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='breed',
            name='avg_weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='building',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cage',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cage',
            name='row',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='chicken',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='chicken',
            name='productivity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='chicken',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='worker',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]