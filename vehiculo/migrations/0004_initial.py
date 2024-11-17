# Generated by Django 5.1.3 on 2024-11-17 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehiculo', '0003_delete_vehiculos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(default='Ford', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.CharField(max_length=50)),
                ('serial_motor', models.CharField(max_length=50)),
                ('categoria', models.CharField(default='Particular', max_length=20)),
                ('precio', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
