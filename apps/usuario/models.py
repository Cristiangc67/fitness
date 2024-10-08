from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Usuario(AbstractUser):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    createDate = models.DateTimeField(auto_now_add=True)
    modificatedDate = models.DateTimeField(auto_now_add=True)
    deleteDate = models.DateTimeField(
        auto_now_add=True
    )  # Chequear como seria esto y falta agregar rolesid
