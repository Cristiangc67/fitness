# Generated by Django 5.1.2 on 2024-11-16 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_alter_medico_previous_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='previous_experience',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]