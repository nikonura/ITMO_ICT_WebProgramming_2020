# Generated by Django 3.1.2 on 2020-10-25 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presencing_publications', '0005_auto_20201025_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='descr',
            field=models.TextField(blank=True, null=True),
        ),
    ]