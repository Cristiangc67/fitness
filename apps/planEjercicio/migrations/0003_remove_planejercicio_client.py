# Generated by Django 5.1.1 on 2024-10-15 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planEjercicio', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planejercicio',
            name='client',
        ),
    ]
