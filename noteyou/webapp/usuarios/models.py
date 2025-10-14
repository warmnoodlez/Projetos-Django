from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# Adiciona campos adicionais para o perfil.
class Usuario(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    foto = models.ImageField(
        upload_to="foto/", # Pasta dentro de MEDIA_ROOT.
        blank=True, null=True
    )

    def __str__(self):
        return self.username