from django.db import models


# Create your models here.
class PlanAlimentacion(models.Model):
    client = models.ForeignKey("cliente.Cliente", on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    modificatedDate = models.DateTimeField(auto_now_add=True)
    deleteDate = models.DateTimeField(auto_now_add=True)


# un cliente puede tener un solo plan de alimentacion y un plan de alimentacion
# deberia tener varios usuarios si incluimos client aca tenemos que definir
# un plan de alimentacion diferente para cada cliente.

# Talvez deberiamos agregar un nombre para plan
