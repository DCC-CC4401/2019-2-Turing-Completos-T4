from os import path, remove

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Custom filename
def get_filename(instance, filename):
    name = 'user_images/' + str(instance.user.id)
    extension = '.' + filename.split('.')[-1]
    fullname = path.join(settings.MEDIA_ROOT, name)
    # TODO: Checkear todas las extensiones de imagen con el fullname
    img_extensions = ['.png', '.jpg', '.jpeg', '.svg']
    for ext in img_extensions:
        if path.exists(fullname + ext):
            remove(fullname + ext)
    return name + extension


# User Profile Model
class UserProfile(models.Model):
    image = models.ImageField(upload_to=get_filename)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, default='1')
    name = models.CharField(max_length=25, default=' ')
    lastname = models.CharField(max_length=25, default=' ')

    def __str__(self):
        return self.user.email


class Amigos(models.Model):
    correo1 = models.ForeignKey(UserProfile, models.SET_NULL, null=True, blank=True, related_name='Amigo1')
    correo2 = models.ForeignKey(UserProfile, models.SET_NULL, null=True, blank=True, related_name='Amigo2')
    estado = models.CharField(max_length=10)

    def __str__(self):
        return self.estado


class Actividades(models.Model):
    correo1 = models.ForeignKey(UserProfile, models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20)

    class Meta:
        ordering = ['correo1', 'categoria']

    def __str__(self):
        return self.nombre


class CreacionActividad(models.Model):
    correo1 = models.ForeignKey(UserProfile, models.SET_NULL, null=True, blank=True)
    nombre = models.ForeignKey(Actividades, models.SET_NULL, null=True, blank=True)
    inicio = models.DateTimeField()
    termino = models.DateTimeField()

    class Meta:
        ordering = ['correo1', 'inicio']

    def __str__(self):
        return self.nombre
