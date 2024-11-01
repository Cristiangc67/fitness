# Generated by Django 5.1.1 on 2024-10-15 22:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('planAlimentacion', '0002_initial'),
        ('planEjercicio', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='others',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='planAlimentacion',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='planAlimentacion.planalimentacion'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='planEjercicio',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='planEjercicio.planejercicio'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
