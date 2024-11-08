from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Conversacion(models.Model):
    client = models.ForeignKey(
        "cliente.Cliente", on_delete=models.CASCADE, related_name="conversaciones"
    )
    doctor = models.ForeignKey(
        "medico.Medico", on_delete=models.CASCADE, related_name="conversaciones"
    )
    created_by = models.ForeignKey(
        "usuario.Usuario",
        on_delete=models.CASCADE,
        related_name="conversaciones_created_by",
    )
    created = models.DateTimeField(auto_now_add=True)
    modificated = models.DateTimeField(null=True, blank=True)
    delete = models.DateTimeField(null=True, blank=True)


class Mensaje(models.Model):
    conversation = models.ForeignKey(
        "conversacion.Conversacion", on_delete=models.CASCADE
    )
    message = models.CharField(max_length=2000)
    sender = models.ForeignKey("usuario.Usuario", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modificated = models.DateTimeField(auto_now=True)
    delete = models.DateTimeField(null=True, blank=True)
