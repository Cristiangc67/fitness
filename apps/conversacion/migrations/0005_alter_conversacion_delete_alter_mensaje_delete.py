# Generated by Django 5.1.2 on 2024-11-18 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversacion', '0004_alter_conversacion_delete_alter_mensaje_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversacion',
            name='delete',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='delete',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
