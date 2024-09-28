from django.db import models
from apps.usuario.models import Usuario


# Create your models here.
class Medico(Usuario):
    licenseNumber = models.IntegerField(max_length=6)
    specialty = models.CharField(max_length=100)
    previousExperience = models.CharField(max_length=500)
