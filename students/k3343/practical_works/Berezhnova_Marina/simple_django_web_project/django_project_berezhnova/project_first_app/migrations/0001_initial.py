# Generated by Django 3.0.4 on 2020-03-22 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacture', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('gosnumber', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Auto')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('license_type', models.CharField(choices=[('A', 'LIC_A'), ('B', 'LIC_B'), ('C', 'LIC_C')], default='A', max_length=1)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Driver')),
            ],
        ),
    ]
