from django.db import models
from ..accounts.models import UserProfile
# Create your models here.

class Tema(models.Model):
    nome = models.CharField('Nome', max_length=200)

class Status(models.Model):
    nome = models.CharField('Nome', max_length=200)

class Projeto(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    ementa = models.CharField('Ementa', max_length=280)
    descritivo = models.TextField('Descritivo', max_length=500)
    justificativa = models.CharField('Ementa', max_length=280)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    apoiador = models.ManyToManyField(UserProfile)