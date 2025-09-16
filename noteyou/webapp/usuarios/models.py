from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Usuario(AbstractUser):
    # Campos adicionais, se quiser
    #username = models.CharField(max_length=15, blank=True, null=True)
    # bio = models.TextField(blank=True, null=True)
    foto = models.ImageField(
        upload_to="foto/",   # pasta dentro de MEDIA_ROOT
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username