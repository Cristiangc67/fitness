from django.db import models


# Create your models here.
class PlanEjercicio(models.Model):
    client = models.ForeignKey("cliente.Cliente", on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    modificatedDate = models.DateTimeField(auto_now_add=True)
    deleteDate = models.DateTimeField(auto_now_add=True)
