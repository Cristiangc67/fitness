from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Usuario(AbstractUser):

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    create = models.DateTimeField(auto_now_add=True)
    modificated = models.DateTimeField(auto_now=True)
    delete = models.DateTimeField(null=True, blank=True)

    # Cambia los campos de grupos y permisos para evitar conflictos
    """ groups = models.ManyToManyField(
        "auth.Group",
        related_name="usuarios",  # Cambia el related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="usuarios_permissions",  # Cambia el related_name
        blank=True,
    ) """

    def __str__(self):
        return f"{self.name}-   {self.last_name } - {self.email}"
