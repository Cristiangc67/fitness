# Generated by Django 5.1.1 on 2024-11-08 20:33

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('license_number', models.IntegerField()),
                ('specialty', models.CharField(max_length=100)),
                ('previous_experience', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('usuario.usuario',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
