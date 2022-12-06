from django.db import models
from django.contrib.auth.models import User

class Perfiles(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars/', null=True, blank=True)
    sobremi = models.TextField()
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return f'{self.user} | Perfil Nro. {self.id}'

