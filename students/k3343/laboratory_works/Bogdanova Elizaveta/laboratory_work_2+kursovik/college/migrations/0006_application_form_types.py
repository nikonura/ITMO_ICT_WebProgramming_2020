# Generated by Django 3.0 on 2020-06-22 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_auto_20200621_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='form_types',
            field=models.CharField(blank=True, choices=[('Очная', 'Очная'), ('Очно-заочная', 'Очно-Заочная'), ('Заочная', 'Заочная')], default='Очная', max_length=100, verbose_name='Форма обучения'),
        ),
    ]