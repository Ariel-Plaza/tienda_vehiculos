# Generated by Django 5.1.3 on 2024-11-17 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0002_rename_vehiculo_vehiculos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vehiculos',
        ),
    ]
