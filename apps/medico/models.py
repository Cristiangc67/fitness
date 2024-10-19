from django.db import models
from apps.usuario.models import Usuario


# Create your models here.
class Medico(Usuario):
    license_number = models.IntegerField()
    specialty = models.CharField(max_length=100)
    previous_experience = models.CharField(max_length=500)
