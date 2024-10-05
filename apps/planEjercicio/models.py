from django.db import models


# Create your models here.
class PlanEjercicio(models.Model):
    client = models.ForeignKey("cliente.Cliente", on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    modificatedDate = models.DateTimeField(auto_now_add=True)
    deleteDate = models.DateTimeField(auto_now_add=True)


# un cliente puede tener un solo plan de ejercicio y un plan de ejercicio
# deberia tener varios usuarios si incluimos client aca tenemos que definir
# un plan de ejercicio diferente para cada cliente.

# cada cliente ya tiene una foreign Key de los planes que elige
