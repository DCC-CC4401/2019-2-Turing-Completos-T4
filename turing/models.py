from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class UsuarioConRoll(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    roll = models.CharField(max_length=10)

    def __str__(self):
        return self.user.email

class Amigos(models.Model):
    correo1 = models.ForeignKey(UsuarioConRoll, models.SET_NULL, null=True, blank=True,related_name='Amigo1')
    correo2 = models.ForeignKey(UsuarioConRoll, models.SET_NULL, null=True, blank=True, related_name='Amigo2')
    estado = models.CharField(max_length=10)

    def __str__(self):
        return self.estado


class Actividades(models.Model):
    correo1 = models.ForeignKey(UsuarioConRoll, models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20)


    class metadata:
        ordering =['correo1','categoria']


    def __str__(self):
        return self.nombre


class CreacionActividad(models.Model):
    correo1 = models.ForeignKey(UsuarioConRoll, models.SET_NULL, null=True, blank=True)
    nombre = models.ForeignKey(Actividades, models.SET_NULL, null=True, blank=True)
    inicio = models.DateTimeField()
    termino = models.DateTimeField()

    class metadata:
        ordering = ['correo1','inicio']


    def __str__(self):
        return self.nombre



