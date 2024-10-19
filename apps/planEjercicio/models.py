from django.db import models


# Create your models here.
class PlanEjercicio(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modificated = models.DateTimeField(auto_now_add=True)
    delete = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, null=True, blank=True)


# un cliente puede tener un solo plan de ejercicio y un plan de ejercicio
# deberia tener varios usuarios si incluimos client aca tenemos que definir
# un plan de ejercicio diferente para cada cliente.

# cada cliente ya tiene una foreign Key de los planes que elige
