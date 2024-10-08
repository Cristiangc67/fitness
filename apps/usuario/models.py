from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Usuario(AbstractUser):
    # Puedes quitar estos campos, si no son necesarios
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    # email ya está incluido en AbstractUser
    # password ya está incluido en AbstractUser

    createDate = models.DateTimeField(auto_now_add=True)
    modificatedDate = models.DateTimeField(auto_now=True)  # Cambié a auto_now
    deleteDate = models.DateTimeField(
        null=True, blank=True
    )  # Permite que sea nulo al eliminar

    # Cambia los campos de grupos y permisos para evitar conflictos
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="usuarios",  # Cambia el related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="usuarios_permissions",  # Cambia el related_name
        blank=True,
    )

    def __str__(self):
        return f"{self.name}-   {self.lastname } - {self.email}"
