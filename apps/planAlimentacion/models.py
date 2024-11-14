from django.db import models


# Create your models here.
class PlanAlimentacion(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modificated = models.DateTimeField(auto_now_add=True)
    delete = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, null=True, blank=True)


# un cliente puede tener un solo plan de alimentacion y un plan de alimentacion
# deberia tener varios usuarios si incluimos client aca tenemos que definir
# un plan de alimentacion diferente para cada cliente.

# Talvez deberiamos agregar un nombre para plan
