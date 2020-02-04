from django.db import models
from ..accounts.models import UserProfile
# Create your models here.

DEFAULT_STATUS = 1

class Tema(models.Model):
    nome = models.CharField('Nome', max_length=200)

    def __str__(self):
        return(self.nome)

class Status(models.Model):
    nome = models.CharField('Nome', max_length=200)

    def __str__(self):
        return(self.nome)

class Projeto(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    ementa = models.CharField('Ementa', max_length=280)
    descritivo = models.TextField('Descritivo', max_length=500)
    justificativa = models.CharField('Justificativa', max_length=280)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=DEFAULT_STATUS)
    concordo = models.BooleanField(default=False)
    apoiador = models.ManyToManyField(UserProfile)

    def __str__(self):
        return(self.ementa)