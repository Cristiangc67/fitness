# Generated by Django 5.1.1 on 2024-10-19 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_cliente_assigned_medico'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='planAlimentacion',
            new_name='plan_alimentacion',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='planEjercicio',
            new_name='plan_ejercicio',
        ),
    ]