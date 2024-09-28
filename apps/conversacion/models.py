from django.db import models


# Create your models here.
class Conversacion(models.Model):
    message = models.CharField(max_length=2000)
    client = models.ForeignKey("cliente.Cliente", on_delete=models.CASCADE)
    doctor = models.ForeignKey("medico.Medico", on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    modificatedDate = models.DateTimeField(auto_now_add=True)
    deleteDate = models.DateTimeField(auto_now_add=True)
