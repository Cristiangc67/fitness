# Generated by Django 5.1.2 on 2024-11-16 00:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('planAlimentacion', '0001_initial'),
        ('planEjercicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='plan_alimentacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planAlimentacion.planalimentacion'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='plan_ejercicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planEjercicio.planejercicio'),
        ),
    ]
