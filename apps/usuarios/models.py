from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=11)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)

    