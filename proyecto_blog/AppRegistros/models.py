from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f'{self.user} | Avatar'

class Personal(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    biografia = models.TextField()
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return f'{self.user} | About'