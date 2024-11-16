from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


# Create your models here.
class Usuario(AbstractUser):

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True)
    modificated = models.DateTimeField(auto_now=True)
    delete = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("perfil", args=[str(self.id)])

    def __str__(self):
        return f"{self.name}-   {self.last_name } - {self.email}"
