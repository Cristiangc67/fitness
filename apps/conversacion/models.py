from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Conversacion(models.Model):
    message = models.CharField(max_length=2000)
    client = models.ForeignKey("cliente.Cliente", on_delete=models.CASCADE)
    doctor = models.ForeignKey("medico.Medico", on_delete=models.CASCADE)
    sender_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    sender_object_id = models.PositiveIntegerField()
    sender = GenericForeignKey("sender_content_type", "sender_object_id")
    createdDate = models.DateTimeField(auto_now_add=True)
    modificatedDate = models.DateTimeField(auto_now_add=True)
    deleteDate = models.DateTimeField(auto_now_add=True)
